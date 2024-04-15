import unittest

from app.riddle.logic.condition_generator import generate_all_matrices, _reshape_to_matrix


class TestRiddleFunctions(unittest.TestCase):
    def test_generate_all_matrices(self):
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
        self.fail("Matrix {} not found in generated matrices".format(has_matrix))

    def test_reshape_to_matrix(self):
        # Test case: 1D slice to 2D matrix
        input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        res = _reshape_to_matrix(input_data, 3)
        self.assertEqual(res, expected, "Reshaped matrix is not as expected")

