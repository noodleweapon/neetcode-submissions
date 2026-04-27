class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = left = 0
        right, bottom = len(matrix[0]), len(matrix)
        res = []
        def in_bounds():
            return top < bottom and left < right
        
        while True:
            for c in range(left, right):
                res.append(matrix[top][c])
            top += 1
            if not in_bounds():
                break
            for r in range(top, bottom):
                res.append(matrix[r][right - 1])
            right -= 1
            if not in_bounds():
                break
            for c in reversed(range(left, right)):
                res.append(matrix[bottom - 1][c])
            bottom -= 1
            if not in_bounds():
                break
            for r in reversed(range(top, bottom)):
                res.append(matrix[r][left])
            left += 1
            if not in_bounds():
                break

        return res