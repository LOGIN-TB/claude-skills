"""Packaging and CLI regression checks for Apple HIG; no app conformance claim."""
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'apple-hig'
SCRIPT = SKILL / 'scripts' / 'validate_audit.py'


class AppleHigPackageTests(unittest.TestCase):
    def test_frontmatter_and_name(self):
        content = (SKILL / 'SKILL.md').read_text()
        self.assertTrue(content.startswith('---\nname: apple-hig\n'))
        self.assertIn('# Apple HIG\n', content)
        self.assertNotIn('metadata:\n  hermes:', content)

    def test_marketplace_entry(self):
        market = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text())
        entries = [x for x in market['plugins'] if x['name'] == 'apple-hig']
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]['skills'], ['./skills/apple-hig'])
        self.assertEqual(entries[0]['source'], './')
        self.assertIs(entries[0]['strict'], False)

    def test_local_skill_references_exist(self):
        paths = re.findall(r'`((?:references|templates|scripts)/[^`]+)`', (SKILL / 'SKILL.md').read_text())
        self.assertGreaterEqual(len(paths), 9)
        for path in paths:
            with self.subTest(path=path):
                self.assertTrue((SKILL / path).is_file())

    def test_source_inventory_and_citations(self):
        inventory = (SKILL / 'references/source-map.md').read_text()
        ids = set(map(int, re.findall(r'^## .* \[(\d+)\]$', inventory, re.M)))
        self.assertEqual(ids, set(range(1, 174)))
        for path in [SKILL / 'SKILL.md', *SKILL.glob('references/*.md')]:
            for source in re.findall(r'\[(\d+)\]', path.read_text()):
                self.assertIn(int(source), ids, str(path))

    def test_no_old_name_or_private_paths(self):
        for path in SKILL.rglob('*'):
            if path.is_file() and path.suffix in {'.md', '.json', '.py'}:
                text = path.read_text()
                for forbidden in ('apple-hig-implementation', '/Users/bot/', '.hermes/', '518355906'):
                    self.assertNotIn(forbidden, text, str(path))

    def test_documentation_links(self):
        paths = [ROOT / 'docs/apple-hig-anleitung.md', SKILL / 'README.md']
        for path in paths:
            for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
                if '://' in target or target.startswith('#'):
                    continue
                self.assertTrue((path.parent / target.split('#')[0]).exists(), f'{path}: {target}')

    def test_unfilled_template_is_rejected(self):
        result = subprocess.run([sys.executable, str(SCRIPT), str(SKILL / 'templates/hig-audit.json')], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('not_tested', result.stdout)

    def test_cli_valid_synthetic_fixture(self):
        fixture = {'project': 'Synthetic test', 'scope': 'Validator only', 'expected_ids': ['A'], 'criteria': [{'id': 'A', 'requirement': 'Synthetic rule', 'origin': 'engineering', 'source_ids': [], 'status': 'pass', 'evidence': ['synthetic-reference'], 'reason': ''}]}
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'audit.json'
            path.write_text(json.dumps(fixture))
            result = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('NOT verified', result.stdout)


def load_tests(loader, tests, pattern):
    """Include the portable validator suite in repository-wide discovery."""
    scripts = str(SKILL / 'scripts')
    sys.path.insert(0, scripts)
    try:
        spec = importlib.util.spec_from_file_location('apple_hig_validator_tests', SKILL / 'scripts/test_validate_audit.py')
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        tests.addTests(loader.loadTestsFromModule(module))
    finally:
        sys.path.remove(scripts)
    return tests


if __name__ == '__main__':
    unittest.main()
