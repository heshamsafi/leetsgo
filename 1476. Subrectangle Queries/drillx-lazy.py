from dataclasses import dataclass

@dataclass
class RectangleUpdate:
    row1: int
    col1: int
    row2: int
    col2: int
    newValue: int

class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rec = rectangle
        self.updates = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.updates.append(RectangleUpdate(row1, col1, row2, col2, newValue))

    def getValue(self, row: int, col: int) -> int:
        # If the value has been updated return the latest update
        for update in reversed(self.updates):
            if update.row1 <= row <= update.row2 and update.col1 <= col <= update.col2:
                return update.newValue

        # If the cell hasn't been updated return the original cell value
        return self.rec[row][col]

# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
