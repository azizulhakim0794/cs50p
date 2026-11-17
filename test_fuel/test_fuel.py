# pytest test_fuel.py
import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("6") == 6


def test_gauge():
    assert gauge(20) == "20"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

    with pytest.raises(ValueError):
        convert("-1/4")


def test_negative():
    with pytest.raises(ValueError):
        convert("-1/4")

    with pytest.raises(ValueError):
        convert("1/-4")


def test_invalid_fraction():
    with pytest.raises(ValueError):
        convert("5/4")

    with pytest.raises(ValueError):
        convert("abc/4")
