import base64
from . import main


def test_s1c1_hex2b64():
    hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    data = bytes.fromhex(hex_str)
    expected = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    result = base64.b64encode(data).decode("ascii")

    assert result == expected
    print("s1c1: ", result)


def test_s1c2_fixed_xor():
    data1 = bytes.fromhex("1c0111001f010100061a024b53535009181c")
    data2 = bytes.fromhex("686974207468652062756c6c277320657965")
    expected = bytes.fromhex("746865206b696420646f6e277420706c6179")

    result = bytes(a ^ b for a, b in zip(data1, data2))

    assert result == expected
    print(result)


def test_int2ascii():
    data = bytes.fromhex("48656c6c6f20576f726c6421")
    expected = "Hello World!"

    result = data.decode("ascii")

    assert result == expected


