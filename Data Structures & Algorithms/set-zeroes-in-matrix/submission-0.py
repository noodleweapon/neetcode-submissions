class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rs = set()
        cs = set()
        R = len(matrix)
        C = len(matrix[0])

        for r in range(R):
            for c in range(C):
                cell = matrix[r][c]
                if cell == 0:
                    rs.add(r)
                    cs.add(c)
    

        for r in rs:
            for c in range(C):
                matrix[r][c] = 0

        for c in cs:
            for r in range(R):
                matrix[r][c] = 0