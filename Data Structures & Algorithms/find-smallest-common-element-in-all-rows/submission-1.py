class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        R, C = len(mat), len(mat[0])

        def bs(r, i, target): # found, left
            j = C - 1
            while i <= j:
                m = (i + j) // 2
                v = mat[r][m]
                if v < target:
                    i = m + 1
                elif v > target:
                    j = m - 1
                else:
                    return True, i
            return False, i - 1

        left_inds = [0] * R
        for c in range(C):
            target = mat[0][c]
            all_found = True
            for r in range(1, R):
                found, i = bs(r, left_inds[r], target)
                left_inds[r] = i
                if not found:
                    all_found = False
            if all_found:
                return target
        return -1