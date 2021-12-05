from pathlib import Path
from typing import Generator


def load(day: int) -> Generator[str, None, None]:
    data_file = Path(__file__).parent / f"day{day}.txt"
    with data_file.open("rt") as file_stream:
        for line in file_stream:
            yield line.strip()
