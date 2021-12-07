from aoc2021.data.provider import load

data = [int(x) for x in next(load(day=7)).split(",")]


def score(pos: int) -> int:
    ret = 0
    for d in data:
        dp = abs(d - pos)
        ret += int((dp * (dp + 1)) / 2)
    return ret


best_pos = 0
best = 1000000000
for i in range(0, 1000):
    sc = score(i)
    if sc < best:
        best = sc
        best_pos = i
print(f"Lowest fuel is {best} at position {best_pos}")
