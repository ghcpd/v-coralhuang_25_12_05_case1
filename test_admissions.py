import pytest
from admissions import validate_student_id, compute_aggregate, qualify_choice, suggest_programs


def test_validate_student_id_valid():
    assert validate_student_id('UG20250001')


def test_validate_student_id_invalid():
    assert not validate_student_id('UG20251')
    assert not validate_student_id('AB20250001')


def test_compute_aggregate():
    scores = {'Math': 10, 'Eng': 12, 'Sci': 8}
    assert compute_aggregate(scores) == 30


def test_compute_aggregate_no_scores():
    with pytest.raises(ValueError):
        compute_aggregate({})


def test_qualify_choice_first_exact_cutoff():
    assert qualify_choice(50, [50, 40, 30]) == 'First'


def test_qualify_choice_second():
    assert qualify_choice(45, [50, 40, 30]) == 'Second'


def test_qualify_choice_none():
    assert qualify_choice(25, [50, 40, 30]) == 'None'


def test_suggest_programs():
    programs = [
        {'name': 'A', 'cutoff': 20},
        {'name': 'B', 'cutoff': 50},
        {'name': 'C', 'cutoff': 30},
    ]
    matches = suggest_programs(25, programs)
    assert len(matches) == 1
    assert matches[0]['name'] == 'A'
