#!/usr/bin/env python3
"""Validate HIG audit completeness, never actual application conformance.

Exit 0: declared criteria complete and passing/not applicable.
Exit 1: incomplete, failing, invalid or blocked audit. Stdlib only.
"""
import json
import sys
from pathlib import Path

STATUSES = {'pass', 'fail', 'not_tested', 'blocked', 'not_applicable'}
ORIGINS = {'hig', 'engineering', 'product'}


def validate(data):
    errors = []
    if not isinstance(data, dict):
        return ['audit must be a JSON object']
    for field in ('project', 'scope'):
        value = data.get(field)
        if not isinstance(value, str) or not value.strip() or 'REPLACE_' in value:
            errors.append(f'{field}: real nonempty value required')
    expected = data.get('expected_ids')
    if not isinstance(expected, list) or not expected or not all(isinstance(x, str) and x.strip() for x in expected):
        errors.append('expected_ids: nonempty list of nonempty strings required')
        expected = []
    if len(expected) != len(set(expected)):
        errors.append('expected_ids: duplicate IDs')
    criteria = data.get('criteria')
    if not isinstance(criteria, list) or not criteria:
        errors.append('criteria: nonempty list required')
        criteria = []
    actual = []
    for index, row in enumerate(criteria):
        if not isinstance(row, dict):
            errors.append(f'criteria[{index}]: object required')
            continue
        rid = row.get('id')
        if not isinstance(rid, str) or not rid.strip():
            errors.append(f'criteria[{index}]: nonempty id required')
            rid = f'<invalid-{index}>'
        actual.append(rid)
        requirement = row.get('requirement')
        if not isinstance(requirement, str) or not requirement.strip():
            errors.append(f'{rid}: requirement missing')
        if row.get('origin') not in ORIGINS:
            errors.append(f'{rid}: invalid origin')
        sources = row.get('source_ids')
        if not isinstance(sources, list) or not all(type(x) is int and 1 <= x <= 173 for x in sources):
            errors.append(f'{rid}: source_ids must reference source-map IDs 1..173')
        elif row.get('origin') == 'hig' and not sources:
            errors.append(f'{rid}: HIG rule needs source_ids')
        status = row.get('status')
        if status not in STATUSES:
            errors.append(f'{rid}: invalid status')
        elif status not in {'pass', 'not_applicable'}:
            errors.append(f'{rid}: unresolved status {status}')
        evidence = row.get('evidence')
        if not isinstance(evidence, list) or not all(isinstance(x, str) and x.strip() for x in evidence):
            errors.append(f'{rid}: evidence must be a list of nonempty strings')
        elif status == 'pass' and not evidence:
            errors.append(f'{rid}: pass requires evidence references')
        reason = row.get('reason')
        if status != 'pass' and (not isinstance(reason, str) or not reason.strip()):
            errors.append(f'{rid}: non-pass status requires reason')
    if len(actual) != len(set(actual)):
        errors.append('criteria: duplicate IDs')
    missing = set(expected) - set(actual)
    extra = set(actual) - set(expected)
    if missing:
        errors.append('missing criteria: ' + ', '.join(sorted(missing)))
    if extra:
        errors.append('unexpected criteria: ' + ', '.join(sorted(extra)))
    return errors


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 validate_audit.py PROJECT/hig-audit.json', file=sys.stderr)
        return 1
    try:
        data = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
        errors = validate(data)
    except (OSError, ValueError, TypeError) as exc:
        print(f'INVALID: {exc}', file=sys.stderr)
        return 1
    if errors:
        print('\n'.join('FAIL: ' + error for error in errors))
        return 1
    print(f'PASS: {len(data["criteria"])} declared criteria accounted for. Evidence content and app conformance NOT verified.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
