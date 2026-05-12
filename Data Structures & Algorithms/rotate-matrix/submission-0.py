class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for edge in range(n // 2):
            for i in range(edge, n - edge - 1):
                E = n - 1
                matrix[edge][i], matrix[i][E - edge], matrix[E - edge][E - i], matrix[E - i][edge] = matrix[E - i][edge], matrix[edge][i], matrix[i][E - edge], matrix[E - edge][E - i]
