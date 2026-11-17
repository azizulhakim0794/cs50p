from twttr import shorten


def test_twttr():
    assert shorten("Twitter") == "Twttr"
    assert shorten("hello") == "hll"
    assert shorten("AEIOU") == ""
    assert shorten("CUSTOMER") == "CSTMR"
    assert shorten("123") == "123"
    assert shorten("HelP?") == "HlP?"
