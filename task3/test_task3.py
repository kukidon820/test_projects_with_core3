from solution import appearance


def test_appearance_no_overlap():
    intervals = {
        'lesson': [100, 200],
        'pupil': [50, 60, 70, 80],
        'tutor': [90, 95]
    }
    assert appearance(intervals) == 0


def test_appearance_full_overlap():
    intervals = {
        'lesson': [100, 200],
        'pupil': [100, 200],
        'tutor': [100, 200]
    }
    assert appearance(intervals) == 100


def test_appearance_multiple_intervals():
    intervals = {
        'lesson': [100, 200],
        'pupil': [110, 120, 130, 140, 150, 160],
        'tutor': [115, 125, 135, 145, 155, 165]
    }
    assert appearance(intervals) == 15


def test_appearance_edge_cases():
    intervals = {
        'lesson': [100, 200],
        'pupil': [99, 101, 199, 201],
        'tutor': [100, 200]
    }
    assert appearance(intervals) == 2


def test_appearance_empty_intervals():
    intervals = {
        'lesson': [100, 200],
        'pupil': [],
        'tutor': [100, 200]
    }
    assert appearance(intervals) == 0
