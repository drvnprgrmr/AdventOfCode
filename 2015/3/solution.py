from argparse import ArgumentParser
from os import path
from sys import stderr

from aocd.models import Puzzle

YEAR: int = 2015
DAY: int = 3

puzzle = Puzzle(YEAR, DAY)

parser = ArgumentParser("Advent of Code solution file")
parser.add_argument("-t", "--test", action="store_true")


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
    current_position_tuple = tuple(current_position)  # add the starting postion

    visited_positions.add(current_position_tuple)

    for dir in data:
        if dir == "^":  # up
            current_position[1] += 1
        elif dir == "v":  # down
            current_position[1] -= 1
        elif dir == ">":  # right
            current_position[0] += 1
        elif dir == "<":  # left
            current_position[0] -= 1

        # check if position has been visited previously
        current_position_tuple = (current_position[0], current_position[1])
        visited_positions.add(current_position_tuple)

    return visited_positions.__len__()


def solve_b(raw_data: str) -> int:
    visited_positions = set()
    santa_position = [0, 0]  # x, y
    robo_santa_position = [0, 0]  # x, y

    # add the starting postion
    current_position_tuple = tuple(santa_position)
    visited_positions.add(current_position_tuple)

    current_santa = santa_position
    for dir in data:
        if dir == "^":  # up
            current_santa[1] += 1
        elif dir == "v":  # down
            current_santa[1] -= 1
        elif dir == ">":  # right
            current_santa[0] += 1
        elif dir == "<":  # left
            current_santa[0] -= 1

        # switch santas
        current_santa = (
            robo_santa_position if current_santa == santa_position else santa_position
        )

        # check if position has been visited previously
        current_position_tuple = (current_santa[0], current_santa[1])
        visited_positions.add(current_position_tuple)

    return visited_positions.__len__()


if __name__ == "__main__":
    data = load_input_data()

    # load parser's arguments
    args = parser.parse_args()

    if not puzzle.answered("a"):
        answer_a = solve_a(data)
        if not args.test:
            puzzle.answer_a = answer_a
        else:
            print(answer_a)

    elif not puzzle.answered("b"):
        answer_b = solve_b(data)
        if not args.test:
            puzzle.answer_b = answer_b
        else:
            print(answer_b)
