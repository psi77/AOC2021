from aoc2021.data.provider import load

DIM = 1000

grid = [[0] * DIM for i in range(DIM)]


def plot_grid():
    for dx in range(0, DIM):
        print("".join([str(p) for p in grid[dx]]))


for line in load(day=5, test=False):
    pieces = line.split("->")
    froms = pieces[0].split(",")
    tos = pieces[1].split(",")

    fromX = int(froms[0].strip())
    fromY = int(froms[1].strip())
    toX = int(tos[0].strip())
    toY = int(tos[1].strip())

    r = max(abs(toX - fromX), abs(toY - fromY))
    dx = int((toX - fromX) / r)
    dy = int((toY - fromY) / r)
    sx = fromX
    sy = fromY
    # print(fromX, fromY, toX, toY)
    # print(dx, dy, sx, sy, r)
    for i in range(0, r + 1):
        grid[sx][sy] += 1
        sx += dx
        sy += dy

    # plot_grid()
    # print()

    # if fromX == toX:
    #     # print(f"{fromX} {fromY} {toX} {toY}")
    #     for i in range(min(fromY, toY), max(fromY, toY) + 1):
    #         grid[fromX][i] += 1
    # elif fromY == toY:
    #     # print(f"{fromX} {fromY} {toX} {toY}")
    #     for i in range(min(fromX, toX), max(fromX, toX) + 1):
    #         grid[i][fromY] += 1

count = 0
for x in range(0, DIM):
    for y in range(0, DIM):
        if grid[x][y] > 1:
            count += 1
print(f"Count: {count}")
