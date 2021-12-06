from collections import defaultdict
from dataclasses import dataclass
from typing import List

from aoc2021.data.provider import load


class Fish:
    def __init__(self) -> None:
        self._counts = defaultdict(int)

    def add_fish(self, age: int) -> None:
        self._counts[age] = self._counts[age] + 1

    def next(self) -> "Fish":
        zero = self._counts[0]
        for i in range(1, 9):
            self._counts[i - 1] = self._counts[i]
        self._counts[8] = zero
        self._counts[6] = self._counts[6] + zero
        return self

    def __len__(self) -> int:
        # print(self._counts)
        return sum(self._counts.values())


@dataclass
class State:
    day: int
    fish: Fish


def next_state(state: State):
    return State(day=state.day + 1, fish=state.fish.next())


if __name__ == "__main__":
    data = [int(x) for x in next(load(day=6)).split(",")]
    # data = [3, 4, 3, 1, 2]
    start = Fish()
    for t in data:
        start.add_fish(t)
    state = State(day=0, fish=start)
    while state.day != 256:
        state = next_state(state)
        print(state.day)
    print(f"Day: {state.day}, No. of fish: {len(state.fish)}")
