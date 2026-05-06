from os import path
from sys import stderr

from aocd.models import Puzzle

YEAR: int = 2015
DAY: int = 3

puzzle = Puzzle(YEAR, DAY)

testing = False


def load_input_data() -> str:
    try:
        with open(path.join(path.dirname(__file__), "input.txt")) as f:
            input_data = f.read()
    except FileNotFoundError:
        input_data = puzzle.input_data
        with open(path.join(path.dirname(__file__), "input.txt"), "x") as f:
            f.write(input_data)

    return input_data


def solve_a(raw_data: str) -> int:
    visited_positions = set()
    current_position = [0, 0]  # x, y
    revisit_count = 0

    for dir in data:
        if dir == "^":  # up
            current_position[1] += 1
        elif dir == "v":  # down
            current_position[1] -= 1
        elif dir == ">":  # right
            current_position[0] += 1
        elif dir == "<":  # left
            current_position[0] -= 1
        else:
            print(f"unrecognised character: {dir}", file=stderr)
            exit()

        # check if position has been visited previously
        current_position_tuple = (current_position[0], current_position[1])
        if current_position_tuple in visited_positions:
            revisit_count += 1
        else:
            visited_positions.add(current_position_tuple)

    return revisit_count


def solve_b(raw_data: str) -> int:
    return 0


if __name__ == "__main__":
    data = load_input_data()

    if not puzzle.answered("a"):
        answer_a = solve_a(data)
        if not testing:
            puzzle.answer_a = answer_a
        else:
            print(answer_a)

    elif not puzzle.answered("b"):
        answer_b = solve_b(data)
        if not testing:
            puzzle.answer_b = answer_b
        else:
            print(answer_b)
