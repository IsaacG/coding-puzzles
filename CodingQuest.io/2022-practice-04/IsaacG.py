#!/bin/python

"""CodingQuest.io 2022 Practice 04: Lost in transmission.

https://codingquest.io/problem/16
"""

import os
import pathlib


def solve(data: str) -> int:
    # Parse. Extract rows and columns.
    grid = [[int(char, 16) for char in line.split()] for line in data.splitlines()]
    rows = grid[:-1]
    columns = list(zip(*grid))[:-1]
    # Find the row error.
    for idx, (*vals, checksum) in enumerate(rows):
        if diff := sum(vals) % 256 - checksum:
            row_idx, row_diff = idx, diff
            break
    # Find the column error and compute the answer.
    for idx, (*vals, checksum) in enumerate(columns):
        if sum(vals) % 256 != checksum:
            correct = (vals[row_idx] - row_diff) % 256
            return correct * vals[row_idx]


if __name__ == "__main__":
    day_num = int(pathlib.Path(__file__).parent.stem.split("-")[-1]) + 12
    paths = [
        pathlib.Path(__file__).parent / "example_data",
        pathlib.Path(os.getenv("HOME")) / "coding_quest_inputs" / f"{day_num}.txt",
    ]
    for path in paths:
        data = path.read_text()
        print(solve(data))
