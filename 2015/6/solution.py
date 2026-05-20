import re
from argparse import ArgumentParser
from enum import Enum
from functools import reduce
from os import path

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


# -------------------------------------------------------------
MATRIX_LEN = 1000
light_matrix = [[False for i in range(MATRIX_LEN)] for j in range(MATRIX_LEN)]


class Action(Enum):
    TURN_ON = 0
    TURN_OFF = 1
    TOGGLE = 2


def execute_action(action: Action, tl: str, br: str) -> None:
    top, left = tl.split(",")
    top, left = int(top), int(left)

    bottom, right = br.split(",")
    bottom, right = int(bottom), int(right)

    # flip order if rectangle is reversed
    if top > bottom:
        top, bottom = bottom, top
        left, right = right, left

    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if action == Action.TURN_ON:
                light_matrix[i][j] = True
            elif action == Action.TURN_OFF:
                light_matrix[i][j] = False
            elif action == Action.TOGGLE:
                light_matrix[i][j] = not light_matrix[i][j]


coord_regex = re.compile(r"(\d+,\d+).*?(\d+,\d+)")


def process_instruction(line: str) -> None:
    # decode string
    rect_top_left, rect_bottom_right = re.findall(coord_regex, line)[0]
    if line.startswith("turn on"):
        execute_action(Action.TURN_ON, rect_top_left, rect_bottom_right)
    elif line.startswith("turn off"):
        execute_action(Action.TURN_OFF, rect_top_left, rect_bottom_right)
    elif line.startswith("toggle"):
        execute_action(Action.TOGGLE, rect_top_left, rect_bottom_right)


def get_on_lights() -> int:
    on_lights = 0
    for i in range(MATRIX_LEN):
        on_lights += reduce(lambda x, y: x + y, light_matrix[i])
    return on_lights


def solve_a(data: str) -> int:
    for line in data.splitlines():
        process_instruction(line)

    return get_on_lights()


# ------------------------------------------------


def process_instruction_differently(line: str) -> None:
    # decode string
    rect_top_left, rect_bottom_right = re.findall(coord_regex, line)[0]
    if line.startswith("turn on"):
        execute_updated_action(Action.TURN_ON, rect_top_left, rect_bottom_right)
    elif line.startswith("turn off"):
        execute_updated_action(Action.TURN_OFF, rect_top_left, rect_bottom_right)
    elif line.startswith("toggle"):
        execute_updated_action(Action.TOGGLE, rect_top_left, rect_bottom_right)


def execute_updated_action(action: Action, tl: str, br: str) -> None:
    top, left = tl.split(",")
    top, left = int(top), int(left)

    bottom, right = br.split(",")
    bottom, right = int(bottom), int(right)

    # flip order if rectangle is reversed
    if top > bottom:
        top, bottom = bottom, top
        left, right = right, left

    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if action == Action.TURN_ON:
                var_brightness_matrix[i][j] += 1
            elif action == Action.TURN_OFF and var_brightness_matrix[i][j]:
                var_brightness_matrix[i][j] -= 1
            elif action == Action.TOGGLE:
                var_brightness_matrix[i][j] += 2


def get_total_brightness() -> int:
    total_brightness = 0
    for i in range(MATRIX_LEN):
        total_brightness += reduce(lambda x, y: x + y, var_brightness_matrix[i])
    return total_brightness


var_brightness_matrix = [[0 for i in range(MATRIX_LEN)] for j in range(MATRIX_LEN)]


def solve_b(data: str) -> int:
    for line in data.splitlines():
        process_instruction_differently(line)
    return get_total_brightness()


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
