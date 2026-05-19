import token
from argparse import ArgumentParser
from os import path

from aocd.examples import Example
from aocd.models import Puzzle

YEAR: int = 2015
DAY: int = 5

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


unwanted_strings = ("ab", "cd", "pq", "xy")


def has_unwanted_strings(string: str) -> bool:
    for unwanted_string in unwanted_strings:
        if unwanted_string in string:
            return True
    return False


def has_at_least_three_vowels(string: str) -> bool:
    vowel_count = 0
    for char in string:
        if char in "aeiou":
            vowel_count += 1
            if vowel_count == 3:
                return True
    return False


def has_at_least_one_duplicate(string: str) -> bool:
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return True
    return False


def solve_a(data: str) -> int:
    lines = data.split()
    nice_string_count = 0

    for string in lines:
        if has_unwanted_strings(string):
            continue
        elif has_at_least_one_duplicate(string) and has_at_least_three_vowels(string):
            nice_string_count += 1

    return nice_string_count


def has_pair_twice(string: str) -> bool:
    tokens: list[str] = []
    for i in range(len(string) - 1):
        tokens.append(string[i] + string[i + 1])

    for p1 in range(len(tokens) - 2):
        for p2 in range(p1 + 2, len(tokens)):
            if tokens[p1] == tokens[p2]:
                return True
    return False


def has_letter_sandwich(string: str) -> bool:
    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            return True

    return False


def solve_b(data: str) -> int:
    lines = data.split()
    nice_string_count = 0

    for line in lines:
        if has_pair_twice(line) and has_letter_sandwich(line):
            nice_string_count += 1

    return nice_string_count


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
