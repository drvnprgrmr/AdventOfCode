from functools import reduce
from os import path

from aocd.models import Puzzle

YEAR: int = 2015
DAY: int = 2

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


def solve_a(data: str) -> int:
    total_wrapping_paper_area: int = 0
    for line in data.splitlines():
        length, width, height = line.split("x")
        length = int(length)
        width = int(width)
        height = int(height)

        side_area_1 = length * width
        side_area_2 = length * height
        side_area_3 = width * height

        smallest_side_area = min(side_area_1, side_area_2, side_area_3)

        total_wrapping_paper_area += (
            2 * side_area_1 + 2 * side_area_2 + 2 * side_area_3 + smallest_side_area
        )

    return total_wrapping_paper_area


def solve_b(data: str) -> int:
    total_ribbon_length = 0
    for line in data.splitlines():
        length, width, height = line.split("x")

        length = int(length)
        width = int(width)
        height = int(height)

        dimensions = [length, width, height]
        dimensions.sort()

        wrapping_ribbon_length = 2 * (dimensions[0] + dimensions[1])
        bow_ribbon_length = reduce(lambda prev, next: prev * next, dimensions)

        print(dimensions, sep=", ")
        print(wrapping_ribbon_length, bow_ribbon_length)

        total_ribbon_length += wrapping_ribbon_length + bow_ribbon_length

    return total_ribbon_length


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
