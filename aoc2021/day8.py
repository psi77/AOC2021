from aoc2021.data.provider import load

count = 0
unique_lengths = [2, 3, 4, 7]
for line in load(day=8, test=False):
    bits = line.split("|")
    _solve = bits[0].strip()
    _digits = bits[1].strip()
    digits = _digits.split(" ")
    for dd in digits:
        if len(dd) in unique_lengths:
            count += 1

print(count)
