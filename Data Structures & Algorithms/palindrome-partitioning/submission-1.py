class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        dp = {} # i: []

        def is_pal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def rec(i, arr):
            if i == n:
                res.append(arr.copy())
                return
            for j in range(i, n):
                if is_pal(i, j):
                    arr.append(s[i:j+1])
                    rec(j + 1, arr)
                    arr.pop()

        rec(0, [])
        return res



        # Input: s = "aab"
        # Output: [["a","a","b"],["aa","b"]]
