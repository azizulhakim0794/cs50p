import pytest
from week8.working import convert

def main():
    test_full_time()
    test_value_error()

def test_full_time():
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"

def test_value_error():
    with pytest.raises(ValueError):
        convert("10 to 8:50 PM")

    with pytest.raises(ValueError):
            convert("14 AM to 80:50 PM")

    with pytest.raises(ValueError):
            convert("15 AM 8:50 PM")
