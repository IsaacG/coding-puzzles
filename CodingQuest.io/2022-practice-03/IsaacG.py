#!/bin/python

"""CodingQuest.io 2022 Practice 03: Survey an asteroid belt.

https://codingquest.io/problem/15
"""

import os
import pathlib


def solve(data: str) -> int:
    weight_map = {
        complex(x, y): int(size)
        for y, line in enumerate(data.splitlines())
        for x, size in enumerate(line.split())
        if size != "0"
    }

    directions = [complex(1, 0), complex(-1, 0), complex(0, 1), complex(0, -1)]
    weights = []
    not_done = set(weight_map)
    while not_done:
        todo = {not_done.pop()}
        weight = 0
        while todo:
            pos = todo.pop()
            not_done.discard(pos)
            weight += weight_map[pos]
            neighbors = (pos + d for d in directions)
            todo.update(n for n in neighbors if n in not_done and n in weight_map)
        weights.append(weight)
    return int(sum(weights) / len(weights))


if __name__ == "__main__":
    day_num = int(pathlib.Path(__file__).parent.stem.split("-")[-1]) + 12
    paths = [
        pathlib.Path(__file__).parent / "example_data",
        pathlib.Path(os.getenv("HOME")) / "coding_quest_inputs" / f"{day_num}.txt",
    ]
    for path in paths:
        data = path.read_text()
        print(solve(data))
