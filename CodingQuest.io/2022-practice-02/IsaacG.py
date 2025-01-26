#!/bin/python

"""CodingQuest.io 2022 Practice 01: Snakes and Ladders.

https://codingquest.io/problem/13
"""

import os
import pathlib


def solve(wordlist: list[str], guesses: str) -> int:
    """Solve which player wins and when."""
    # Green: we know which letter is in this position.
    green = [None] * 7
    # Yellow: we know the word must have this letter.
    yellow = set()
    # Yellow position: we know this position is _not_ this letter.
    yellow_pos = [set() for _ in range(7)]
    # Black: this letter is not in the word.
    black = set()
    # Process the guesses.
    for line in guesses.splitlines():
        guess, results = line.split()
        for idx, (letter, color) in enumerate(zip(guess, results)):
            if color == "G":
                green[idx] = letter
            elif color == "B":
                black.add(letter)
            elif color == "Y":
                yellow.add(letter)
                yellow_pos[idx].add(letter)

    want_letters = (set(green) | yellow) - {None}

    # Look for a winning word.
    for word in wordlist:
        letters = set(word)
        # The word may not have any black letters.
        if letters & black:
            continue
        # The word must contain all green and yellow letters.
        if want_letters - letters:
            continue
        # Green letters must be in the correct position.
        if any(known and known != got for known, got in zip(green, word)):
            continue
        # Yellow letters much not be in specific positions.
        if any(got in yellow for yellow, got in zip(yellow_pos, word)):
            continue
        return word


if __name__ == "__main__":
    day_num = int(pathlib.Path(__file__).parent.stem.split("-")[-1]) + 12
    dict_file = pathlib.Path(os.getenv("HOME")) / "coding_quest_inputs" / f"{day_num}.txt"
    dictionary = dict_file.read_text().splitlines()
    data = [
        "hapless GBYYYBB\njackpot BBBBYBB\nfullest YYGYYBB",
        "keyless YYBBYYG\nsociety YGYYYBB\nphobias BBGBGBG",
    ]
    for guess_lines in data:
        print(solve(dictionary, guess_lines))
