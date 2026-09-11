import re
from argparse import ArgumentParser
from collections import defaultdict
from enum import Enum
from os import path
from pprint import pprint

from aocd.examples import Example
from aocd.models import Puzzle

YEAR: int = 2015
DAY: int = 8

puzzle = Puzzle(YEAR, DAY)

parser = ArgumentParser("Advent of Code solution file")
parser.add_argument("-t", "--test", action="store_true")
parser.add_argument("-e", "--example", action="store_true")

# load parser's arguments
args = parser.parse_args()


def load_input_data() -> str:
    try:
        with open(path.join(path.dirname(__file__), "input.txt")) as f:
            input_data = f.read()
    except FileNotFoundError:
        input_data = puzzle.input_data
        with open(path.join(path.dirname(__file__), "input.txt"), "x") as f:
            f.write(input_data)

    return input_data


def save_anwer(data: str, file_suffix: str):
    with open(path.join(path.dirname(__file__), f"answer_{file_suffix}.txt"), "w") as f:
        f.write(data)


# -------------------------------------------------------------


def solve_a(data: str) -> int:
    lines = data.splitlines()
    cumulative_difference = 0
    for line in lines:
        cumulative_difference += len(line) - len(eval(line))  # pyright: ignore[reportAny]

    return cumulative_difference


def solve_b(data: str):
    lines = data.splitlines()
    total_excess = 0
    pattern = re.compile(r"[\"\\]")
    for line in lines:
        total_excess += 2 + len(re.findall(pattern, line))
    return total_excess


# -------------------------------------------------------------


if __name__ == "__main__":
    data = load_input_data()

    if puzzle.answered_a:
        save_anwer(str(puzzle.answer_a), "a")

        # you can only attempt b if you've answered a
        if puzzle.answered_b:
            save_anwer(str(puzzle.answer_b), "b")
        else:
            answer_b = solve_b(data)
            if args.test:
                print(answer_b)
            else:
                if args.example:
                    # make sure examples pass first
                    for example in puzzle.examples:
                        example: Example
                        example_test_answer = str(solve_b(example.input_data))
                        assert example.answer_b == example_test_answer, (
                            "Solution doesn't work for example."
                            + f"\nGot {example_test_answer} instead of {example.answer_b}"
                        )
                puzzle.answer_b = answer_b
    else:
        answer_a = solve_a(data)
        if args.test:
            print(answer_a)
        else:
            if args.example:
                # make sure examples pass first
                for example in puzzle.examples:
                    example_test_answer = str(solve_a(example.input_data))
                    assert example.answer_a == example_test_answer, (
                        "Solution doesn't work for example."
                        + f"\nGot {example_test_answer} instead of {example.answer_a}"
                    )
            puzzle.answer_a = answer_a
