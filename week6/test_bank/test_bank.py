from week6.test_bank.bank import value


def test_value():
    assert value("hello") == 0
    assert value("What's up?") == 100
    assert value("How you Doing?") == 20
    assert value("Hello, newman") == 0
    assert value("What's happening?") == 100
