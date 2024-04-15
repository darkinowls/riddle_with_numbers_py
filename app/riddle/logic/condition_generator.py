from typing import List

from app.riddle.logic.cell import Cell
from app.riddle.logic.riddle import solve_matrix

min_value = 1
max_value = 3
matrix_size = 3


def generate_all_matrices(size: int) -> List[List[List[int]]]:
    matrices = []
    current_matrix = []
    __generate_matrix_helper(matrices, current_matrix, 0, size)
    return matrices


def __generate_matrix_helper(matrices: List[List[List[int]]], current_matrix: List[int], index: int, size: int):
    if index == size * size:
        m = _reshape_to_matrix(current_matrix, size)
        tm = __translate_to_cells(m)
        if not solve_matrix(tm):
            return
        matrices.append(m)
        return

    for i in range(min_value, max_value + 1):
        current_matrix.append(i)
        __generate_matrix_helper(matrices, current_matrix, index + 1, size)
        current_matrix.pop()  # backtrack


def _reshape_to_matrix(matrix: List[int], size: int) -> List[List[int]]:
    res = []
    for i in range(size):
        res.append(matrix[i * size: (i + 1) * size])
    return res


def __translate_to_cells(input_data: List[List[int]]) -> List[List[Cell]]:
    output = []
    for row in input_data:
        cell_row = [Cell(is_marked=True, value=value) for value in row]
        output.append(cell_row)
    return output
