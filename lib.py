from argparse import ArgumentParser
from os import path
from types import FunctionType

from aocd.examples import Example
from aocd.models import Puzzle

YEAR: int = 2015
DAY: int = 6

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


# todo: create solution template


def solve_puzzle(solution_a: FunctionType, solution_b: FunctionType):
    # todo: add generic solution path
    pass


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
