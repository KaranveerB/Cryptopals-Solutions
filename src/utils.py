from collections import defaultdict
from src.data import english_freqs


def int2ascii(val: int) -> str:
    res = ""
    while val:
        res += chr(val & 0xFF)
        val >>= 8
    return "".join(res[::-1])


def is_human_readable(s: str) -> bool:
    for c in s:
        if not (ord(" ") <= ord(c) <= ord("~")):
            return False
    return True


def compute_freq_percent_map(s: str) -> dict[str, float]:
    raw_freq: dict[str, int] = defaultdict(int)
    total = 0
    for c in s:
        if c.isalpha():
            raw_freq[c.lower()] = raw_freq[c.lower()] + 1
            total += 1
    freq: dict[str, float] = {}
    for i in range(26):
        c = chr(ord("a") + i)
        freq[c] = raw_freq[c] / total

    return freq


def compute_english_distance(freq: dict[str, float]) -> float:
    distance = 0.0
    for k, v in english_freqs.items():
        distance += abs(v - freq[k])
    return distance
