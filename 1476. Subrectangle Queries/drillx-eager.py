class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rec = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for r in range(row1, row2+1):
            for c in range(col1, col2+1):
                self.rec[r][c] = newValue

    def getValue(self, r: int, c: int) -> int:
        return self.rec[r][c]

# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
