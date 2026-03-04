import base64

from src import solvers
from . import main


def test_s1c1():
    expected = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    result = solvers.s1c1()
    assert result == expected


def test_s1c2():
    expected = bytes.fromhex("746865206b696420646f6e277420706c6179")
    result = solvers.s1c2()
    assert result == expected


def test_s1c3():
    expected_key = "X"
    expected_str = "Cooking MC's like a pound of bacon"
    result = solvers.s1c3()

    assert result[1] == "X"
    assert result[2] == "Cooking MC's like a pound of bacon"
