# Somehow easier than https://neetcode.io/problems/stone-game-ii/question?list=allNC
import sys
sys.setrecursionlimit(99999)
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = {}
        def rec(i, alice):
            if i >= n:
                return 0
            if (i, alice) in dp:
                return dp[(i, alice)]
            if alice:
                res = float("-inf")
                for x in range(1, 4):
                    value = sum(stoneValue[i:i+x]) + rec(i + x, not alice)
                    res = max(res, value)
            else:
                res = float("inf")
                for x in range(1, 4):
                    value = -sum(stoneValue[i:i+x]) + rec(i + x, not alice)
                    res = min(res, value)
            dp[(i, alice)] = res
            return res

        final = rec(0, True)
        if final > 0:
            return 'Alice'
        elif final < 0:
            return 'Bob'
        else:
            return 'Tie'