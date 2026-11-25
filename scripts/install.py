#!/usr/bin/env python3
"""Install opstack skills without changing client settings. Python 3.9+."""
import argparse
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
TARGETS = {'copilot': '.copilot', 'cursor': '.cursor', 'claude': '.claude', 'codex': '.codex'}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contained(base, relative):
    rel = Path(relative)
    if rel.is_absolute() or '..' in rel.parts:
        raise ValueError('Invalid relative path: ' + str(relative))
    path = base / rel
    if base.resolve() not in path.resolve().parents:
        raise ValueError('Path escapes collection: ' + str(relative))
    for node in [path] + list(path.parents):
        if node == base:
            break
        if node.is_symlink():
            raise ValueError('Symlink in collection: ' + str(node))
    return path


def verify_collection():
    expected = json.loads((ROOT / 'integrity.json').read_text())
    for relative, checksum in expected.items():
        path = contained(ROOT, relative)
        if not path.is_file() or digest(path) != checksum:
            raise ValueError('Collection integrity check failed: ' + relative)
    for node in (ROOT / 'skills').rglob('*'):
        if node.is_symlink():
            raise ValueError('Symlink in core skills: ' + str(node))
    actual = {p.relative_to(ROOT).as_posix() for p in (ROOT / 'skills').rglob('*') if p.is_file()}
    if actual - set(expected):
        raise ValueError('Unexpected skill files: ' + ', '.join(sorted(actual - set(expected))))
    print('Verified {} collection files.'.format(len(expected)))


def file_map(base):
    result = {}
    for p in base.rglob('*'):
        if p.is_symlink():
            raise ValueError('Symlink in skill: ' + str(p))
        if p.is_file():
            result[p.relative_to(base).as_posix()] = digest(p)
    return result


def instructions(src, agent):
    text = (src / 'SKILL.md').read_text(encoding='utf-8')
    if agent in ['copilot', 'cursor']:
        text = re.sub(r'^name: (Presentations|Spreadsheets)[ \t]*$', lambda m: 'name: ' + m[1].lower(), text, flags=re.M)
    return text.encode('utf-8')


def library_skills(base, agent):
    base = base.expanduser().resolve()
    manifest = json.loads((base / 'manifest.json').read_text())
    checks = json.loads((base / 'checksums.json').read_text())
    for row in checks:
        p = contained(base, row['path'])
        if not p.is_file() or digest(p) != row['sha256']:
            raise ValueError('Local library integrity check failed: ' + row['path'])
    hashes = {row['path']: row['sha256'] for row in checks}
    variants = {row['name']: row for row in manifest['skills'] if row.get('variant') and 'claude' in row['path']}
    result = []
    for row in manifest['skills']:
        if row.get('variant'):
            continue
        if agent == 'claude':
            row = variants.get(row['name'], row)
        name = row['name'].lower()
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
            raise ValueError('Invalid library skill name: ' + name)
        source = contained(base, row['path'])
        if not (source / 'SKILL.md').is_file():
            raise ValueError('Missing library skill: ' + name)
        for rel, checksum in file_map(source).items():
            if hashes.get((Path(row['path']) / rel).as_posix()) != checksum:
                raise ValueError('Unverified library file: ' + name + '/' + rel)
        result.append((source, name))
    return result


def domain_skill_available(target, name):
    folder = target / name
    entry = folder / 'SKILL.md'
    if folder.is_symlink() or entry.is_symlink() or not entry.is_file():
        return False
    text = entry.read_text(encoding='utf-8')
    header = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)', text, re.S)
    if not header:
        return False
    field = re.search(r'^name:\s*([^\r\n]+)', header[1], re.M)
    if not field or field[1].strip().strip('"\'').lower() != name:
        return False
    return re.search(r'^description:[ \t]*\S', header[1], re.M) is not None


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--agent', choices=TARGETS, default='copilot')
    parser.add_argument('--target', type=Path, help='Override the personal skill destination')
    parser.add_argument('--library', type=Path, help='Also import a local exported personal skill library')
    parser.add_argument('--only', nargs='+', metavar='SKILL', help='Install selected names only, preserving other installed skills')
    parser.add_argument('--check-library', action='store_true', help='Check whether all 146 domain skills are installed; no writes')
    parser.add_argument('--require-library', action='store_true', help='Refuse setup unless all 146 domain skills will be available')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--verify', action='store_true', help='Check collection only; do not install')
    args = parser.parse_args(argv)
    verify_collection()
    if args.verify:
        return 0
    target = (args.target or Path.home() / TARGETS[args.agent] / 'skills').expanduser().absolute()
    if target.is_symlink():
        raise ValueError('Target is a symlink. Choose its actual directory explicitly.')
    resolved = target.resolve()
    if resolved == ROOT or ROOT in resolved.parents:
        raise ValueError('Choose an installation target outside this repository.')
    selected = [(p, p.name) for p in sorted((ROOT / 'skills').iterdir()) if p.is_dir() and (p / 'SKILL.md').is_file()]
    if args.library:
        library = args.library.expanduser().resolve()
        if library == resolved or library in resolved.parents:
            raise ValueError('Installation target must be outside the imported library.')
        selected += library_skills(library, args.agent)
    catalog = json.loads((ROOT / 'skills/opstack-swarm/references/library-catalog.json').read_text())
    required = {row['installed_name'] for row in catalog['skills']}
    if args.only:
        unknown = set(args.only) - {name for _, name in selected}
        if unknown:
            raise ValueError('Unknown selected skills: ' + ', '.join(sorted(unknown)))
        selected = [(source, name) for source, name in selected if name in args.only]
    available = {name for name in required if domain_skill_available(target, name)}
    if args.check_library:
        missing = required - available
        print('Domain library: {}/{} installed.'.format(len(available), len(required)))
        if missing:
            print('Missing: ' + ', '.join(sorted(missing)))
            return 1
        return 0
    if args.require_library:
        missing = required - available - {name for _, name in selected}
        if missing:
            raise ValueError('Full-stack setup needs the personal archive via --library PATH. Missing domain skills: ' + ', '.join(sorted(missing)))
    if len({name for _, name in selected}) != len(selected):
        raise ValueError('Duplicate skill names in selected sources.')
    pending, conflicts, expected_maps = [], [], {}
    for source, name in selected:
        encoded = instructions(source, args.agent)
        expected = file_map(source)
        expected['SKILL.md'] = hashlib.sha256(encoded).hexdigest()
        expected_maps[name] = expected
        dest = target / name
        if dest.exists() or dest.is_symlink():
            try:
                matches = not dest.is_symlink() and dest.is_dir() and file_map(dest) == expected
            except ValueError:
                matches = False
            if not matches:
                conflicts.append(str(dest))
        else:
            pending.append((source, dest, encoded))
    if conflicts:
        print('No installation changes made. Existing different skills were preserved:\n' + '\n'.join(conflicts), file=sys.stderr)
        print('Reconcile these skills manually or choose another --target.', file=sys.stderr)
        return 1
    print('{}: {} new, {} unchanged -> {}'.format('Plan' if args.dry_run else 'Install', len(pending), len(selected) - len(pending), target))
    if args.dry_run:
        return 0
    target.mkdir(parents=True, exist_ok=True)
    lock = target / '.opstack-install.lock'
    try:
        handle = lock.open('x')
    except FileExistsError:
        raise ValueError('Another or interrupted installation owns ' + str(lock) + '. Confirm it has stopped before removing the lock manually.')
    try:
        with handle:
            handle.write('opstack installation in progress\n')
        for source, dest, encoded in pending:
            # Refuse destinations that appeared after preflight; never merge old files.
            shutil.copytree(source, dest)
            (dest / 'SKILL.md').write_bytes(encoded)
        for _, name in selected:
            if file_map(target / name) != expected_maps[name]:
                raise ValueError('Installed verification failed: ' + name)
    finally:
        lock.unlink()
    print('Verified {} installed skills. Personal instructions and external dependencies are unchanged.'.format(len(selected)))
    print('To activate opstack by default, use DEFAULT-PROMPT.md in this repository.')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
