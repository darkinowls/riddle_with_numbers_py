""" Module for the input/output of the riddle task. """
from app.riddle.logic.cell import Cell


def get_task_init() -> list[list[Cell]]:
    """ Get the initial matrix for the task."""
    matrix = [
        [Cell(1), Cell(1), Cell(4), Cell(3), Cell(4), Cell(1), Cell(3), Cell(2), Cell(2)],
        [Cell(1), Cell(1), Cell(2), Cell(3), Cell(2), Cell(1), Cell(3), Cell(2), Cell(2)],
        [Cell(3), Cell(2), Cell(1), Cell(4), Cell(3), Cell(3), Cell(2), Cell(1), Cell(3)],
        [Cell(4), Cell(3), Cell(4), Cell(2), Cell(3), Cell(1), Cell(1), Cell(2), Cell(4)],
        [Cell(4), Cell(2), Cell(1), Cell(1), Cell(2), Cell(3), Cell(3), Cell(4), Cell(1)],
        [Cell(2), Cell(2), Cell(3), Cell(3), Cell(4), Cell(4), Cell(4), Cell(1), Cell(2)],
        [Cell(2), Cell(3), Cell(3), Cell(1), Cell(3), Cell(2), Cell(2), Cell(4), Cell(1)],
        [Cell(4), Cell(4), Cell(2), Cell(1), Cell(3), Cell(1), Cell(2), Cell(3), Cell(3)],
        [Cell(4), Cell(4), Cell(2), Cell(1), Cell(1), Cell(1), Cell(2), Cell(3), Cell(3)]
    ]
    return matrix


def get_example_init() -> list[list[Cell]]:
    """ Get the example matrix for the task."""
    matrix = [
        [Cell(4), Cell(2), Cell(4), Cell(8)],
        [Cell(8), Cell(6), Cell(6), Cell(8)],
        [Cell(4), Cell(2), Cell(6), Cell(6)],
        [Cell(2), Cell(2), Cell(6), Cell(6)]
    ]
    return matrix


def get_example_result() -> list[list[Cell]]:
    """ Get the example result matrix for the task."""
    matrix = [
        [Cell(4, True), Cell(2, False),
         Cell(4, False), Cell(8, False)],

        [Cell(8, False), Cell(6, False),
         Cell(6, True), Cell(8, True)],

        [Cell(4, False), Cell(2, True),
         Cell(6, True), Cell(6, True)],

        [Cell(2, False), Cell(2, True),
         Cell(6, True), Cell(6, True)]
    ]
    return matrix
