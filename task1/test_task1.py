import pytest
from solution import strict, sum_two


def test_strict_correct_types():
    assert sum_two(1, 2) == 3


def test_strict_incorrect_types():
    with pytest.raises(TypeError):
        sum_two(1, 2.4)


def test_strict_with_kwargs():
    @strict
    def multiply(a: int, b: int) -> int:
        return a * b

    assert multiply(a=2, b=3) == 6
    with pytest.raises(TypeError):
        multiply(a=2.0, b=3)
