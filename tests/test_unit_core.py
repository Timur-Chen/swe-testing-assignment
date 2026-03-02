import pytest
from quick_calc.core import Calculator


def test_addition():
    calc = Calculator()
    assert calc.add(5, 3) == 8


def test_subtraction():
    calc = Calculator()
    assert calc.subtract(10, 4) == 6


def test_multiplication():
    calc = Calculator()
    assert calc.multiply(6, 7) == 42


def test_division():
    calc = Calculator()
    assert calc.divide(8, 2) == 4


def test_division_by_zero():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)


def test_negative_numbers():
    calc = Calculator()
    assert calc.add(-2, -3) == -5


def test_decimal_numbers():
    calc = Calculator()
    assert calc.subtract(1.5, 0.5) == 1.0


def test_large_numbers():
    calc = Calculator()
    assert calc.multiply(10**6, 10**6) == 10**12