class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix)
        C = len(matrix[0])
        n = R * C
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            M = matrix[m // C][m % C]
            if M < target:
                l = m + 1
            elif M > target:
                r = m - 1
            else:
                return True
        return False