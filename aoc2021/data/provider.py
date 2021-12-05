from pathlib import Path
from typing import Generator


def load(day: int, test: bool = False) -> Generator[str, None, None]:
    extra = "_test" if test else ""
    data_file = Path(__file__).parent / f"day{day}{extra}.txt"
    with data_file.open("rt") as file_stream:
        for line in file_stream:
            yield line.strip()
