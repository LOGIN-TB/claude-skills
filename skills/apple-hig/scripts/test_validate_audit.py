#!/usr/bin/env python3
"""Synthetic validator fixtures: not evidence of a real app passing HIG."""
import copy
import unittest
from validate_audit import validate


class AuditTests(unittest.TestCase):
    def setUp(self):
        self.data = {'project': 'Fixture', 'scope': 'Test only', 'expected_ids': ['A'], 'criteria': [{'id': 'A', 'requirement': 'Synthetic test', 'origin': 'hig', 'source_ids': [8], 'status': 'pass', 'evidence': ['synthetic-evidence'], 'reason': ''}]}

    def test_valid(self):
        self.assertEqual(validate(self.data), [])

    def test_not_applicable_with_reason(self):
        self.data['criteria'][0].update(status='not_applicable', evidence=[], reason='Outside project scope')
        self.assertEqual(validate(self.data), [])

    def test_unresolved_statuses(self):
        for status in ('fail', 'not_tested', 'blocked', 'unknown'):
            with self.subTest(status=status):
                d = copy.deepcopy(self.data)
                d['criteria'][0].update(status=status, reason='Fixture')
                self.assertTrue(validate(d))

    def test_missing_evidence(self):
        self.data['criteria'][0]['evidence'] = []
        self.assertTrue(validate(self.data))

    def test_missing_reason(self):
        self.data['criteria'][0].update(status='not_applicable')
        self.assertTrue(validate(self.data))

    def test_duplicate(self):
        self.data['criteria'].append(copy.deepcopy(self.data['criteria'][0]))
        self.assertTrue(validate(self.data))

    def test_missing_id(self):
        self.data['expected_ids'].append('B')
        self.assertTrue(validate(self.data))

    def test_unexpected_id(self):
        self.data['expected_ids'] = ['B']
        self.assertTrue(validate(self.data))

    def test_empty_and_malformed(self):
        for d in (None, [], {}, {'expected_ids': [None], 'criteria': [3]}):
            with self.subTest(d=d):
                self.assertTrue(validate(d))

    def test_bad_sources(self):
        for ids in ([], [174], [True], '8'):
            with self.subTest(ids=ids):
                d = copy.deepcopy(self.data)
                d['criteria'][0]['source_ids'] = ids
                self.assertTrue(validate(d))

    def test_placeholder(self):
        self.data['project'] = 'REPLACE_PROJECT_NAME'
        self.assertTrue(validate(self.data))


if __name__ == '__main__':
    unittest.main()
