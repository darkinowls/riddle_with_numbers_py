from typing import List

from pydantic import BaseModel


class Cell(BaseModel):
    is_marked: bool = True
    value: int

    def __init__(self, value: int, is_marked: bool = True):
        super().__init__(is_marked=is_marked, value=value)


def translate_to_cells(input_data: List[List[int]]) -> List[List[Cell]]:
    num_rows = len(input_data)
    num_cols = len(input_data[0])

    output = []
    for i in range(num_rows):
        row = []
        for j in range(num_cols):
            cell = Cell(is_marked=True, value=input_data[i][j])
            row.append(cell)
        output.append(row)
    return output
