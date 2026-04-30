from os import path

from aocd.models import Puzzle

YEAR: int = 1999
DAY: int = 1

puzzle = Puzzle(YEAR, DAY)

testing = True


def load_input_data() -> str:
    try:
        with open(path.join(path.dirname(__file__), "input.txt")) as f:
            input_data = f.read()
    except FileNotFoundError:
        input_data = puzzle.input_data
        with open(path.join(path.dirname(__file__), "input.txt"), "x") as f:
            f.write(input_data)

    return input_data


def process_input_data(data: str):
    pass


def solve_a(raw_data: str) -> None:
    data = process_input_data(raw_data)
    pass


def solve_b(raw_data: str) -> None:
    data = process_input_data(raw_data)
    pass


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
