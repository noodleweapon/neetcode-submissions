
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        R, K = len(mat1), len(mat1[0])
        K2, C = len(mat2), len(mat2[0])
        res = [[0] * C for _ in range(R)]

        for r in range(R):
            for c in range(C):
                for k in range(K):
                    if mat1[r][k] == 0:
                        continue
                    if mat2[k][c] == 0:
                        continue
                    res[r][c] += mat1[r][k] * mat2[k][c]
        
        return res