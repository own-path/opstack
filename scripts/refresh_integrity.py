#!/usr/bin/env python3
"""Regenerate checksums after intentional repository changes."""
import hashlib
import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
entries = {}
for p in sorted(root.rglob('*')):
    relative = p.relative_to(root)
    if any(part in ['.git', '__pycache__', '.venv'] for part in relative.parts):
        continue
    if p.is_symlink():
        raise ValueError('Symlink in repository: ' + str(relative))
    if not p.is_file() or relative.as_posix() == 'integrity.json' or p.name == '.DS_Store' or p.suffix == '.pyc':
        continue
    entries[relative.as_posix()] = hashlib.sha256(p.read_bytes()).hexdigest()
(root / 'integrity.json').write_text(json.dumps(entries, sort_keys=True, indent=2) + '\n')
print('Recorded {} file checksums.'.format(len(entries)))
