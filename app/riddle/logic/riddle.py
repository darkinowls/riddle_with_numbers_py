"""Riddle logic."""

from .cell import Cell
from .util import duplicate_matrix, is_in_matrix_array, print_matrix


# Розробіть алгоритм вирішення задачі та реалізуйте його у вигляді
# програми мовою Python
# Зафарбуйте деяĸі ĸлітини таĸ, щоб у ĸожному рядĸу або стовпці
# не було чисел, що повторюються. Зафарбовані ĸлітини можуть стиĸатися одна з одною.
# Усі незафарбовані ĸлітини повинні
# з'єднуватися одна з одною сторонами по горизонталі або по
# вертиĸалі таĸ, щоб вийшов єдиний безперервний простір із
# незафарбованих ĸлітин.

###################################################/
# Solve by pathfinding and combining 2 paths

def solve_matrix(matrix) -> list[list[list[Cell]]] | None:
    """Solve the matrix."""
    if len(matrix) == 0 or len(matrix[0]) == 1 or len(matrix) == 1:
        return None

    solutions_down = []

    for i in range(len(matrix[0])):
        down_matrcies = make_way_down(duplicate_matrix(matrix), 0, i)
        solutions_down.extend(down_matrcies)

    solutions_right = []

    for i in range(len(matrix)):
        right_matrices = make_way_right(duplicate_matrix(matrix), i, 0)
        solutions_right.extend(right_matrices)

    solutions = []

    # Combine the ways and check if it doesn't break the rules
    for solution_down in solutions_down:
        for solution_right in solutions_right:
            combined = combine_matrices(solution_down, solution_right)
            if (iterate_matrix_and_check_if_good(combined)
                    and not is_in_matrix_array(combined, solutions)):
                solutions.append(combined)

    return solutions if solutions else None


def make_way_down(origin_matrix, init_row, init_column) -> list[list[list[Cell]]]:
    """Make a way down."""
    print_matrix(origin_matrix)
    solutions = explore_matrix(origin_matrix, init_row, init_column)
    return [solution for solution in solutions if check_if_touches_bottom_wall(solution)]


def make_way_right(origin_matrix, init_row, init_column) -> list[list[list[Cell]]]:
    """Make a way right."""
    solutions = explore_matrix(origin_matrix, init_row, init_column)
    return [solution for solution in solutions if check_if_touches_right_wall(solution)]


def explore_matrix(start_matrix: list[list[Cell]], start_row, start_column) \
        -> list[list[list[Cell]]]:
    """Explore the matrix."""
    solutions = []

    def explore(matrix, row: int, column: int):
        matrix[row][column].is_marked = False

        for drow, dcol in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + drow, column + dcol

            if new_row < 0 or new_row >= len(matrix) or new_col < 0 or new_col >= len(matrix[0]):
                continue

            if not matrix[new_row][new_col].is_marked:
                continue

            if check_if_unique_within_unmarked(matrix, new_row, new_col):
                new_matrix = duplicate_matrix(matrix)
                solutions.append(new_matrix)
                explore(new_matrix, new_row, new_col)

    solutions = []
    explore(start_matrix, start_row, start_column)
    return solutions


#############################################################################
# Compare matrix by matrix

def iterate_matrix_and_check_if_good(matrix):
    """Iterate the matrix and check if it's good."""
    start_col = 0
    for i in range(len(matrix[0])):
        if not matrix[0][i].is_marked:
            start_col = i
            break

    is_good = True
    visited = set()

    def iterate(row, col):
        """Iterate the matrix."""
        nonlocal is_good
        if ((row, col) in visited or row < 0 or col < 0
                or row >= len(matrix) or col >= len(matrix[0])):
            return

        if not matrix[row][col].is_marked:
            return

        visited.add((row, col))

        if not check_if_unique_within_unmarked(matrix, row, col):
            is_good = False
            return

        iterate(row + 1, col)
        iterate(row - 1, col)
        iterate(row, col + 1)
        iterate(row, col - 1)

    iterate(0, start_col)
    return is_good


def check_if_unique_within_unmarked(matrix, row_index, column_index):
    """Check if unique within unmarked."""
    value = matrix[row_index][column_index].value
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if j == column_index or i == row_index:
                if (j, i) == (column_index, row_index):
                    continue
                if cell.value == value and not cell.is_marked:
                    return False
    return True


def get_matrix_column(matrix, column_number):
    """Get a matrix column."""
    return [row[column_number] for row in matrix]


def check_side(solution):
    """Check the side."""
    return any(not cell.is_marked for cell in solution)


def check_if_touches_bottom_wall(solution):
    """Check if touches the bottom wall."""
    return check_side(solution[-1])


def check_if_touches_right_wall(solution):
    """Check if touches the right wall."""
    return check_side(get_matrix_column(solution, len(solution[0]) - 1))


def combine_matrices(matrix1, matrix2):
    """Combine matrices."""
    combined = duplicate_matrix(matrix1)
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            if not matrix2[i][j].is_marked:
                combined[i][j].is_marked = False
    return combined
