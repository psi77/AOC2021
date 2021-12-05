from functools import reduce

from aoc2021.data.provider import load


def part1():
    count, _ = reduce(
        lambda c, n: (c[0] + (1 if int(n) > c[1] else 0), int(n)),
        load(day=1),
        (0, 1000000),
    )
    print(f"{count} increases")


if __name__ == "__main__":
    part1()
