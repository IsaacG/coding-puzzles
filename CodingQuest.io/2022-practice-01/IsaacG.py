#!/bin/python

"""CodingQuest.io 2022 Practice 01: Snakes and Ladders.

https://codingquest.io/problem/13
"""

import os
import pathlib


def solve(data: str) -> int:
    """Solve which player wins and when."""
    board_data = [line for line in data.splitlines() if len(line.split()) > 2]
    dice_data = [line for line in data.splitlines() if len(line.split()) == 2]
    board = []
    for idx, line in enumerate(reversed(board_data)):
        nums = [int(i) for i in line.split()]
        if idx % 2:
            nums.reverse()
        board.extend(nums)
    end = len(board) - 1

    position = {1: 0, 2: 0}
    for moves, line in enumerate(dice_data, start=1):
        for player, roll in enumerate((int(i) for i in line.split()), start=1):
            while roll != 0:
                position[player] += roll
                if position[player] >= end:
                    return player * moves
                roll = board[position[player]]


if __name__ == "__main__":
    day_num = int(pathlib.Path(__file__).parent.stem.split("-")[-1]) + 12
    paths = [
        pathlib.Path(__file__).parent / "example_data",
        pathlib.Path(os.getenv("HOME")) / "coding_quest_inputs" / f"{day_num}.txt",
    ]
    for path in paths:
        data = path.read_text()
        print(solve(data))
