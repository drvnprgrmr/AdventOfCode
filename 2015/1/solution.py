from aocd.models import Puzzle

from os import path


puzzle = Puzzle(2015, 1)


def load_input_data() -> str:
    try:
        with open(path.join(path.dirname(__file__), "input.txt")) as f:
            input_data = f.read()
    except FileNotFoundError:
        input_data = puzzle.input_data
        with open(path.join(path.dirname(__file__), "input.txt"), "x") as f:
            f.write(input_data)

    return input_data


def solve_a(data: str) -> int:
    floor: int = 0
    for char in data:
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1

    return floor


def solve_b(data: str) -> int:
    floor: int = 0
    steps: int = 0
    for char in data:
        steps += 1

        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1

        # Check if we've reached the basement
        if floor == -1:
            break

    return steps


if __name__ == "__main__":
    data = load_input_data()

    if not puzzle.answered("a"):
        puzzle.answer_a = solve_a(data)
    if not puzzle.answered("b"):
        puzzle.answer_b = solve_b(data)
