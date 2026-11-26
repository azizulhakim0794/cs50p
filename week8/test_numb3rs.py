# pytest test_numb3rs.py

from numb3rs import validate

def test_validate():

    assert validate("1.2.3.4") == True
    assert validate("1.2.3") == False
    assert validate("1.2") == False
    assert validate("1") == False
    assert validate("512.1.1.1") == False
    assert validate("1.512.1.1") == False
    assert validate("1.1.512.1") == False
    assert validate("1.1.1.512") == False
    assert validate("255.255.255.255") == True