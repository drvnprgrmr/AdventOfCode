from argparse import ArgumentParser
from collections import defaultdict
from enum import Enum
from os import path
from pprint import pprint

from aocd.examples import Example
from aocd.models import Puzzle

YEAR: int = 2015
DAY: int = 7

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

wire_values = defaultdict[str, int](lambda: -1)
input_wires: list[str] = []


def solve_a(data: str) -> int:
    lines = data.splitlines()
    unprocessed_count = len(lines)
    processed_lines = [False for _ in range(unprocessed_count)]

    while unprocessed_count:
        for i, line in enumerate(lines):
            if processed_lines[i]:  # skip this line if it's been processed already
                continue

            tokens = line.split()  # split line into tokens for parsing
            if len(tokens) == 3:  # This is an initial wire assignment
                left = tokens[0]
                out = tokens[2]

                if left.isnumeric():
                    # update the wire
                    input_wires.append(out)
                    wire_values[out] = int(left)

                elif wire_values[left] == -1:
                    continue

                else:
                    wire_values[out] = wire_values[left]

                # mark line as processed
                unprocessed_count -= 1
                processed_lines[i] = True

            elif len(tokens) == 4:  # process the NOT operation
                left = tokens[1]
                out = tokens[3]

                if left.isnumeric():
                    left = int(left)
                elif wire_values[left] == -1:
                    continue
                else:
                    left = wire_values[left]

                # perform operation
                wire_values[out] = 0xFFFF ^ left

                # mark line as processed
                unprocessed_count -= 1
                processed_lines[i] = True

            elif len(tokens) == 5:
                left = tokens[0]
                op = tokens[1]
                right = tokens[2]
                output = tokens[4]

                # check left input
                if left.isnumeric():
                    left = int(left)
                elif wire_values[left] == -1:
                    continue
                else:
                    left = wire_values[left]

                # check right input
                if right.isnumeric():
                    right = int(right)
                elif wire_values[right] == -1:
                    continue
                else:
                    right = wire_values[right]

                # perform operation
                if op == "AND":
                    wire_values[output] = left & right
                elif op == "OR":
                    wire_values[output] = left | right
                elif op == "LSHIFT":
                    wire_values[output] = left << int(right)
                elif op == "RSHIFT":
                    wire_values[output] = left >> int(right)

                # mark line as processed
                unprocessed_count -= 1
                processed_lines[i] = True

    return wire_values["a"]


# --------------------------------------------------------------


def solve_b(data: str) -> int:
    # set the value of b to a
    wire_values["b"] = solve_a(data)

    # reset all other values
    for key in wire_values.keys():
        if key != "b":
            wire_values[key] = -1

    print("Debug")
    pprint(wire_values)

    # re-solve part a
    return solve_a(data)
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
