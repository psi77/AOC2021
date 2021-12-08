from collections import defaultdict

from aoc2021.data.provider import load

total = 0
unique_lengths = {2: 1, 3: 7, 4: 4, 7: 8}
lcd = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}
for line in load(day=8, test=False):
    print(line)
    bits = line.split("|")
    _solve = bits[0].strip()
    _digits = bits[1].strip()
    digits = _digits.split(" ")

    mapping = {}
    known = {}
    counts = defaultdict(int)
    for s in _solve.split(" "):
        if len(s) in unique_lengths:
            known[unique_lengths[len(s)]] = s
        for letter in s:
            counts[letter] += 1
    print(known)
    print(counts)
    known_top = next(iter(set(known[7]) - set(known[1])))
    mapping[known_top] = "a"
    for k, v in counts.items():
        if v == 4:
            mapping[k] = "e"
        elif v == 6:
            mapping[k] = "b"
        elif v == 9:
            mapping[k] = "f"
        elif v == 8 and k != known_top:
            mapping[k] = "c"
        elif v == 7:
            mapping[k] = "d" if k in set(known[4]) else "g"
    print(mapping)

    dcount = 0
    multi = 1000
    for dd in digits:
        lookup = "".join(sorted([mapping[k] for k in dd]))
        value = lcd[lookup]
        print(f"{lookup} {value}")
        dcount += multi * value
        multi = multi / 10
    total += dcount

print(total)
