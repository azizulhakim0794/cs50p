# python test_plates.py

from week6.test_plates.plates import is_valid


def test_plates():
    assert is_valid("H") == False
    assert is_valid("CS50") == True
    assert is_valid("duZYos") == True
    assert is_valid("123453") == False
    assert is_valid("....") == False
    assert is_valid("CS05") == False
    assert is_valid("PI3.14") == False
    assert is_valid("CS50A") == False
    assert is_valid("AB123") == True
    assert is_valid("AA1A") == False
    assert is_valid("AA01") == False
