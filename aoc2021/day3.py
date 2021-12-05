from functools import reduce

from aoc2021.data.provider import load

gamma = list(
    map(
        lambda r: int(
            "".join(["1" if r[v] > r[0] / 2 else "0" for v in range(1, 13)]), 2
        ),
        [
            reduce(
                lambda c, n: (c[0] + 1, *[c[x + 1] + int(n[x]) for x in range(0, 12)]),
                load(day=3),
                (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            )
        ],
    )
)[0]

epsilon = gamma ^ int("111111111111", 2)

print(f"gamma: {gamma} epsilon: {epsilon} power: {gamma * epsilon}")
