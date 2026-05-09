import hashlib
from argparse import ArgumentParser
from os import path

from aocd.examples import Example
from aocd.models import Puzzle

YEAR: int = 2015
DAY: int = 4

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


def solve_a(secret_key: str) -> str:
    secret_key = secret_key.strip()  # remove any newlines

    answer = 0
    hash = ""
    data = ""

    while not hash.startswith("0" * 5):
        answer += 1
        data = secret_key + str(answer)
        hash = hashlib.md5(bytes(data, "ascii")).hexdigest()

    print("Data: ", data)
    print("Hash: ", hash)
    return str(answer)


def solve_b(secret_key: str) -> str:
    secret_key = secret_key.strip()  # remove any newlines

    answer = 0
    hash = ""
    data = ""

    while not hash.startswith("0" * 6):
        answer += 1
        data = secret_key + str(answer)
        hash = hashlib.md5(bytes(data, "ascii")).hexdigest()

    print("Data: ", data)
    print("Hash: ", hash)
    return str(answer)


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
                        assert example.answer_b == solve_b(example.input_data), (
                            "Solution doesn't work for example"
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
                    assert example.answer_a == solve_a(example.input_data), (
                        "Solution doesn't work for example"
                    )
            puzzle.answer_a = answer_a
