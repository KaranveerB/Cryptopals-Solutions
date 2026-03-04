import base64

from src import utils, data


def s1c1() -> str:
    hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    data = bytes.fromhex(hex_str)

    return base64.b64encode(data).decode("ascii")


def s1c2() -> bytes:
    data1 = bytes.fromhex("1c0111001f010100061a024b53535009181c")
    data2 = bytes.fromhex("686974207468652062756c6c277320657965")

    return bytes(a ^ b for a, b in zip(data1, data2))


def _decode_xor_encryption(data: bytes) -> tuple[float, str, str] | None:
    options: list[tuple[float, str, str]] = []
    for key in range(ord(" "), ord("~") + 1):
        result = bytes(a ^ key for a in data)
        try:
            ascii_str = result.decode("ascii")
        except UnicodeDecodeError as _:
            continue
        if utils.is_human_readable(ascii_str):
            freq_map = utils.compute_freq_percent_map(ascii_str)
            score = utils.compute_english_distance(freq_map)
            options.append((score, chr(key), ascii_str))
    if options:
        return min(options)
    else:
        return None


def s1c3() -> tuple[float, str, str]:
    hex_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    data = bytes.fromhex(hex_str)

    result = _decode_xor_encryption(data)
    assert result is not None
    return result


def s1c4() -> tuple[float, str, str]:
    input_file = data.res_dir / "s1c4.txt"
    hex_strs = input_file.read_text().splitlines()

    options: list[tuple[float, str, str]] = []

    for hex_str in hex_strs:
        result = _decode_xor_encryption(bytes.fromhex(hex_str))
        if result is not None:
            options.append(result)
    # TODO: This is wrong. best guess is we're not considering enough for frequnecy anaylsis?
    # penalize non-alpha chars?
    print(options)
    return min(options)
