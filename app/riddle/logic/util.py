""" This module contains utility functions for the riddle logic. """
from app.riddle.logic.cell import Cell


def duplicate_matrix(matrix: list[list[Cell]]) -> list[list[Cell]]:
    """ Duplicate a matrix."""
    duplicate = []
    for row in matrix:
        duplicate_row = [Cell(cell.value, cell.is_marked) for cell in row]
        duplicate.append(duplicate_row)

    return duplicate


def print_matrix(matrix: list[list[Cell]]) -> None:
    """ Print a matrix."""
    print()
    for row in matrix:
        for cell in row:
            if cell.is_marked:
                print(f"*{cell.value:<4}", end=" ")
            else:
                print(f"{cell.value:<5}", end=" ")
        print()


def compare_matrices(matrix1: list[list[Cell]], matrix2: list[list[Cell]]) -> bool:
    """Compare two matrices."""
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return False  # Matrices have different dimensions

    for i, row in enumerate(matrix1):
        for j, cell in enumerate(row):
            if (cell.value != matrix2[i][j].value
                    or cell.is_marked != matrix2[i][j].is_marked):
                return False  # Cells at position (i, j) are different

    return True  # Matrices are identical



def is_in_matrix_array(matrix: list[list[Cell]], matrix_array: list[list[list[Cell]]]) -> bool:
    """ Check if a matrix is in an array of matrices."""
    for m in matrix_array:
        if compare_matrices(matrix, m):
            return True
    return False


def validate_input_matrix(matrix) -> None:
    """ Validate input matrix."""
    if len(matrix) == 0:
        raise ValueError("matrix is empty")
    if len(matrix[0]) == 1 or len(matrix) == 1:
        raise ValueError("matrix is required not a single row or column")
