class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.w = len(matrix[0])
        self.h = len(matrix)
        self.p = [[0] * self.w for _ in range(self.h)]
        print(self.p)

        for x in range(self.w):
            for y in range(self.h):
                self.p[y][x] = 0

                for _x in range(x + 1):
                    for _y in range(y + 1):
                        self.p[y][x] += matrix[_y][_x]

    def getPrefix(self, r, c):
        if c < 0 or r < 0:
            return 0
        return self.p[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        outer = self.getPrefix(row2, col2)
        inner = self.getPrefix(row1 - 1, col1 - 1)
        left = self.getPrefix(row2, col1 - 1)
        right = self.getPrefix(row1 - 1, col2)
        return outer + inner - left - right


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

    # self.p = []
    #         self.w = len(matrix[0])
    #         self.h = len(matrix)
    #         for x in range(self.w):
    #             l = []
    #             s = 0
    #             for y in range(self.h):
    #                 s += matrix[y][x]
    #                 l.append(s)