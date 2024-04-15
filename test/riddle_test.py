import unittest

from riddle.cell import translate_to_cells, Cell
from riddle.riddle import solve_matrix, check_if_unique_within_unmarked, combine_matrices, check_if_touches_right_wall, \
    check_if_touches_bottom_wall, check_side, get_matrix_column
from riddle.riddle_io import get_example_init, get_example_result
from riddle.util import compare_matrices, validate_input_matrix, print_matrix, duplicate_matrix




class TestRiddleFunctions(unittest.TestCase):

    def test_translate_to_cells(self):
        input_data = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected = [
            [Cell(1), Cell(2), Cell(3)],
            [Cell(4), Cell(5), Cell(6)],
            [Cell(7), Cell(8), Cell(9)]
        ]
        output = translate_to_cells(input_data)
        self.assertTrue(compare_matrices(output, expected))

    def test_translate_to_cells_negative(self):
        input_data = [
            [1, 2, 666],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected = [
            [Cell(1), Cell(2), Cell(3)],
            [Cell(4), Cell(5), Cell(6)],
            [Cell(7), Cell(8), Cell(9)]
        ]
        output = translate_to_cells(input_data)
        self.assertFalse(compare_matrices(output, expected))

    def test_solve_matrix(self):
        # Test case with provided example matrix
        example_matrix = get_example_init()
        expected_result = get_example_result()
        solved_matrix = solve_matrix(example_matrix)
        self.assertTrue(compare_matrices(expected_result, solved_matrix[0]))

        # Additional test cases can be added for different scenarios

    def test_check_if_unique_within_unmarked(self):
        matrix = [
            [Cell(is_marked=False, value=1), Cell(is_marked=False, value=2), Cell(is_marked=False, value=3)],
            [Cell(is_marked=False, value=4), Cell(is_marked=False, value=5), Cell(is_marked=False, value=6)],
            [Cell(is_marked=False, value=7), Cell(is_marked=False, value=8), Cell(is_marked=False, value=9)]
        ]
        self.assertTrue(check_if_unique_within_unmarked(matrix, 0, 0))

        matrix[0][1].value = 1
        self.assertFalse(check_if_unique_within_unmarked(matrix, 0, 0))

    def test_solve_matrix_empty_matrix(self):
        empty_matrix = []
        solved_matrix = solve_matrix(empty_matrix)
        self.assertIsNone(solved_matrix)
    #
    def test_get_matrix_column(self):
        matrix = [
            [Cell(value=1), Cell(value=2), Cell(value=3)],
            [Cell(value=4), Cell(value=5), Cell(value=6)]
        ]
        column = get_matrix_column(matrix, 1)
        expected = [Cell(value=2), Cell(value=5)]
        self.assertEqual(len(column), len(expected))
        for i in range(len(column)):
            self.assertEqual(column[i].value, expected[i].value)

    def test_check_side(self):
        solution_true = [Cell(value=1, is_marked=True), Cell(value=2, is_marked=False), Cell(value=3, is_marked=True)]
        self.assertTrue(check_side(solution_true))

        solution_false = [Cell(value=1, is_marked=True), Cell(value=2, is_marked=True), Cell(value=3, is_marked=True)]
        self.assertFalse(check_side(solution_false))

    def test_check_if_touches_bottom_wall(self):
        solution_true = [
            [Cell(value=1, is_marked=False), Cell(value=2, is_marked=False), Cell(value=3, is_marked=False)],
            [Cell(value=4, is_marked=False), Cell(value=5, is_marked=False), Cell(value=6, is_marked=False)],
            [Cell(value=7, is_marked=True), Cell(value=8, is_marked=False), Cell(value=9, is_marked=True)]
        ]
        self.assertTrue(check_if_touches_bottom_wall(solution_true))

        solution_false = [
            [Cell(value=1, is_marked=False), Cell(value=2, is_marked=False), Cell(value=3, is_marked=False)],
            [Cell(value=4, is_marked=False), Cell(value=5, is_marked=False), Cell(value=6, is_marked=False)],
            [Cell(value=7, is_marked=True), Cell(value=8, is_marked=True), Cell(value=9, is_marked=True)]
        ]
        self.assertFalse(check_if_touches_bottom_wall(solution_false))

    def test_check_if_touches_right_wall(self):
        solution_true = [
            [Cell(value=1, is_marked=False), Cell(value=2, is_marked=False), Cell(value=3, is_marked=True)],
            [Cell(value=4, is_marked=False), Cell(value=5, is_marked=False), Cell(value=6, is_marked=True)],
            [Cell(value=7, is_marked=False), Cell(value=8, is_marked=False), Cell(value=9, is_marked=False)]
        ]
        self.assertTrue(check_if_touches_right_wall(solution_true))

        solution_false = [
            [Cell(value=1, is_marked=False), Cell(value=2, is_marked=False), Cell(value=3, is_marked=True)],
            [Cell(value=4, is_marked=False), Cell(value=5, is_marked=False), Cell(value=6, is_marked=True)],
            [Cell(value=7, is_marked=False), Cell(value=8, is_marked=False), Cell(value=9, is_marked=True)]
        ]
        self.assertFalse(check_if_touches_right_wall(solution_false))

    def test_combine_matrices(self):
        matrix1 = [
            [Cell(value=1, is_marked=True), Cell(value=2, is_marked=False)],
            [Cell(value=3, is_marked=False), Cell(value=4, is_marked=True)]
        ]
        matrix2 = [
            [Cell(value=1, is_marked=False), Cell(value=2, is_marked=False)],
            [Cell(value=3, is_marked=False), Cell(value=4, is_marked=True)]
        ]
        expected = [
            [Cell(value=1, is_marked=False), Cell(value=2, is_marked=False)],
            [Cell(value=3, is_marked=False), Cell(value=4, is_marked=True)]
        ]
        result = combine_matrices(matrix1, matrix2)
        self.assertTrue(compare_matrices(result, expected))

    def test_duplicate_matrix(self):
        matrix = [
            [Cell(value=1, is_marked=True), Cell(value=2, is_marked=False)],
            [Cell(value=3, is_marked=False), Cell(value=4, is_marked=True)]
        ]
        duplicate = duplicate_matrix(matrix)
        self.assertTrue(compare_matrices(matrix, duplicate))

    def test_compare_matrices(self):
        matrix1 = [
            [Cell(value=1, is_marked=True), Cell(value=2, is_marked=False)],
            [Cell(value=3, is_marked=False), Cell(value=4, is_marked=True)]
        ]
        matrix2 = [
            [Cell(value=1, is_marked=True), Cell(value=2, is_marked=False)],
            [Cell(value=3, is_marked=False), Cell(value=4, is_marked=True)]
        ]
        self.assertTrue(compare_matrices(matrix1, matrix2))

        matrix3 = [
            [Cell(value=1, is_marked=True), Cell(value=2, is_marked=False)],
            [Cell(value=3, is_marked=False), Cell(value=4, is_marked=True)]
        ]
        matrix4 = [
            [Cell(value=1, is_marked=True), Cell(value=2, is_marked=False)],
            [Cell(value=3, is_marked=False), Cell(value=5, is_marked=True)]
        ]
        self.assertFalse(compare_matrices(matrix3, matrix4))
