from functools import reduce

from aoc2021.data.provider import load

print(
    list(
        map(
            lambda l: l[0] * l[1],
            [
                reduce(
                    lambda p1, p2: (p1[0] + p2[0], p1[1] + p2[1]),
                    map(
                        lambda a: (
                            int(a[1]) if a[0] == "forward" else 0,
                            int(a[1])
                            if a[0] == "down"
                            else -int(a[1])
                            if a[0] == "up"
                            else 0,
                        ),
                        [d.split(" ") for d in load(day=2)],
                    ),
                    (0, 0),
                )
            ],
        )
    )[0]
)

print(
    list(
        map(
            lambda l: l[0] * l[1],
            [
                reduce(
                    lambda p1, p2: (
                        p1[0] + p2[0],
                        p1[1] + (p2[0] * p1[2]),
                        p1[2] + p2[1],
                    ),
                    map(
                        lambda a: (
                            int(a[1]) if a[0] == "forward" else 0,
                            int(a[1])
                            if a[0] == "down"
                            else -int(a[1])
                            if a[0] == "up"
                            else 0,
                        ),
                        [d.split(" ") for d in load(day=2, test=False)],
                    ),
                    (0, 0, 0),
                )
            ],
        )
    )[0]
)
