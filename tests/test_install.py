"""Installer tests use temporary destinations; no real user settings are touched."""
import hashlib
import importlib.util
import io
import json
import re
import shutil
import tempfile
import unittest
import os
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('opstack_install', ROOT / 'scripts/install.py')
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.target = self.base / 'target'

    def run_install(self, *args):
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            return installer.main(['--target', str(self.target), *args])

    def test_dry_run_has_no_writes(self):
        self.assertEqual(self.run_install('--dry-run'), 0)
        self.assertFalse(self.target.exists())

    def test_each_client_installs_and_repeats_without_changes(self):
        for agent in installer.TARGETS:
            self.target = self.base / agent
            self.assertEqual(self.run_install('--agent', agent), 0)
            self.assertEqual(len(list(self.target.glob('*/SKILL.md'))), 12)
            before = installer.file_map(self.target)
            self.assertEqual(self.run_install('--agent', agent), 0)
            self.assertEqual(installer.file_map(self.target), before)
            for skill in self.target.glob('*/SKILL.md'):
                for link in re.findall(r'\]\(([^)#]+)(?:#[^)]*)?\)', skill.read_text()):
                    self.assertTrue((skill.parent / link).is_file(), link)

    def test_conflicts_prevent_all_copying(self):
        existing = self.target / 'opstack-review'
        existing.mkdir(parents=True)
        (existing / 'SKILL.md').write_text('my custom review')
        self.assertEqual(self.run_install(), 1)
        self.assertEqual(list(self.target.iterdir()), [existing])
        self.assertEqual((existing / 'SKILL.md').read_text(), 'my custom review')

    def test_existing_lock_prevents_copying(self):
        self.target.mkdir()
        lock = self.target / '.opstack-install.lock'
        lock.write_text('another installer')
        with self.assertRaisesRegex(ValueError, 'installation owns'):
            self.run_install()
        self.assertEqual(list(self.target.iterdir()), [lock])
        self.assertEqual(lock.read_text(), 'another installer')

    def test_rejects_repo_target(self):
        with self.assertRaisesRegex(ValueError, 'outside this repository'):
            installer.main(['--target', str(ROOT / 'bad'), '--dry-run'])

    def fixture_library(self):
        library = self.base / 'library'
        rows, hashes = [], []
        for variant, name, path in [(False, 'Presentations', 'docs/presentations'), (False, 'pdf', 'docs/pdf'), (True, 'pdf', 'variants/claude/pdf')]:
            skill = library / path
            skill.mkdir(parents=True)
            (skill / 'SKILL.md').write_text('---\nname: ' + name + '\ndescription: test\n---\n' + path)
            rows.append({'name': name, 'path': path, 'variant': variant})
            hashes.append({'path': path + '/SKILL.md', 'sha256': installer.digest(skill / 'SKILL.md')})
        (library / 'manifest.json').write_text(json.dumps({'skills': rows}))
        (library / 'checksums.json').write_text(json.dumps(hashes))
        return library

    def test_library_import_normalizes_copilot_and_selects_claude(self):
        library = self.fixture_library()
        self.assertEqual(self.run_install('--library', str(library)), 0)
        self.assertEqual(len(list(self.target.glob('*/SKILL.md'))), 14)
        self.assertIn('name: presentations\n', (self.target / 'presentations/SKILL.md').read_text())
        self.target = self.base / 'claude'
        self.assertEqual(self.run_install('--agent', 'claude', '--library', str(library)), 0)
        self.assertIn('variants/claude/pdf', (self.target / 'pdf/SKILL.md').read_text())

    def test_tampered_library_refuses_before_writes(self):
        library = self.fixture_library()
        (library / 'docs/pdf/SKILL.md').write_text('modified')
        with self.assertRaisesRegex(ValueError, 'integrity check failed'):
            self.run_install('--library', str(library))
        self.assertFalse(self.target.exists())

    def test_library_path_traversal_refused(self):
        library = self.fixture_library()
        (library / 'checksums.json').write_text(json.dumps([{'path': '../outside', 'sha256': 'bad'}]))
        with self.assertRaisesRegex(ValueError, 'Invalid relative path'):
            self.run_install('--library', str(library))
        self.assertFalse(self.target.exists())

    def test_core_integrity_rejects_tampering(self):
        copy = self.base / 'collection'
        shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns('.git', '__pycache__'))
        (copy / 'skills/opstack-mode/SKILL.md').write_text('changed')
        original = installer.ROOT
        try:
            installer.ROOT = copy
            with self.assertRaisesRegex(ValueError, 'integrity check failed'):
                self.run_install()
        finally:
            installer.ROOT = original
        self.assertFalse(self.target.exists())

    @unittest.skipIf(os.name == 'nt', 'Creating symlinks may require Windows privileges')
    def test_symlink_core_skill_refused(self):
        copy = self.base / 'collection'
        shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns('.git', '__pycache__'))
        (copy / 'skills/unverified-link').symlink_to(ROOT / 'skills/opstack-mode', target_is_directory=True)
        original = installer.ROOT
        try:
            installer.ROOT = copy
            with self.assertRaisesRegex(ValueError, 'Symlink in core skills'):
                self.run_install()
        finally:
            installer.ROOT = original
        self.assertFalse(self.target.exists())

    def test_manifests_and_names(self):
        for client in ['cursor', 'claude', 'codex']:
            data = json.loads((ROOT / ('.' + client + '-plugin') / 'plugin.json').read_text())
            self.assertEqual(data['name'], 'opstack')
            self.assertTrue((ROOT / data['skills']).is_dir())
        for skill in (ROOT / 'skills').glob('*/SKILL.md'):
            self.assertRegex(skill.read_text(), r'(?m)^name: ' + skill.parent.name + r'$')


if __name__ == '__main__':
    unittest.main()
