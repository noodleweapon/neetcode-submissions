class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R = len(matrix)
        C = len(matrix[0])

        zero_1st_col = False
        for r in range(R):
            if matrix[r][0] == 0:
                zero_1st_col = True
                
        zero_1st_row = False
        for c in range(C):
            if matrix[0][c] == 0:
                zero_1st_row = True

        for r in range(1, R):
            for c in range(1, C):
                cell = matrix[r][c]
                if cell == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
    
        for r in range(1, R):
            if matrix[r][0] == 0:
                for c in range(1, C):
                    matrix[r][c] = 0
        
        for c in range(1, C):
            if matrix[0][c] == 0:
                for r in range(1, R):
                    matrix[r][c] = 0

        if zero_1st_row:
            for c in range(C):
                matrix[0][c] = 0

        if zero_1st_col:
            for r in range(R):
                matrix[r][0] = 0
