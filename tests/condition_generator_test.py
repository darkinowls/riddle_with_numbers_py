"""Tests for the riddle logic functions."""

import unittest

from app.riddle.logic.condition_generator import generate_all_matrices, _reshape_to_matrix


class TestRiddleFunctions(unittest.TestCase):
    """Tests for the riddle logic functions."""

    def test_generate_all_matrices(self):
        """Test the generation of all matrices."""
        # Test case: size 2 matrix
        has_matrix = [
            [2, 1],
            [1, 2]
        ]

        matrices = generate_all_matrices(2)
        self.assertGreaterEqual(len(matrices), 20, "Expected at least 20 matrices")
        for m in matrices:
            if m == has_matrix:
                return
        self.fail(f"Matrix {has_matrix} not found in generated matrices")

    def test_reshape_to_matrix(self):
        """Test the reshaping of a matrix."""
        # Test case: 1D slice to 2D matrix
        input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        res = _reshape_to_matrix(input_data, 3)
        self.assertEqual(res, expected, "Reshaped matrix is not as expected")
