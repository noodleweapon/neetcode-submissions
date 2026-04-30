class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Y = len(matrix)
        X = len(matrix[0])

        def read(i):
            y = int(i / Y)
            x = i - y * Y
            return matrix[y][x]
        
        last_i = X * Y - 1
        i = 0
        j = last_i
        while i <= j:
            if i < 0 or j < 0:
                return False
            if i > last_i or j > last_j:
                return False
            k = (i + j) // 2
            m = read(k)
            if m == target:
                return True
            elif m < target:
                i = k + 1
            else:
                j = k - 1
        return False