class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        R = len(matrix)
        C = len(matrix[0])
        arr = []
        for edge in range(min(R, C) // 2 + 1):
            for c in range(edge, C - edge):
                arr.append(matrix[edge][c])
            for r in range(1 + edge, R - 1 - edge):
                arr.append(matrix[r][C - 1 - edge])
            
            if edge != R - 1 - edge:
                for c in reversed(range(edge, C - edge)):
                    arr.append(matrix[R - 1 - edge][c])
            if edge != C - 1 - edge:
                for r in reversed(range(1 + edge, R - 1 - edge)):
                    arr.append(matrix[r][edge])

        return arr