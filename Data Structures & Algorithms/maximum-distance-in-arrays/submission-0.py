class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        L, U = arrays[0][0], arrays[0][-1]
        M = 0
        for array in arrays[1:]:
            M = max(M, U - array[0], array[-1] - L)
            L = min(L, array[0])
            U = max(U, array[-1])
        return M

        # [1,2], [-2, -1]
        # L=1,U=2
        #         2 - (-2), -1 - (1)
        #         = 4, 0

        # [1,2,3],[-40,5],[1,2,3]
        # L=1,U=3
        #         abs(5 - 1, 3 - (-40))