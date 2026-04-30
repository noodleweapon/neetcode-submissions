class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Y = len(matrix)
        X = len(matrix[0])

        def read(i):
            y = int(i / Y)
            x = i - y * Y
            return matrix[y][x]
        
        i = 0
        j = X * Y - 1
        while i <= j:
            k = (i + j) // 2
            m = read(k)
            if m == target:
                return True
            elif m < target:
                i = k + 1
            else:
                j = k - 1
        return False