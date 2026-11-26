import pytest
from week8.um import count

def test_count_um():

    assert count("Um, thanks, um...") == 2
    assert count(" um ") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("umbrella") == 0
    assert count("UM UM um") == 3
    assert count("yummy") == 0
    assert count("") == 0