class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n, total = len(matchsticks), sum(matchsticks)
        if total % 4 != 0:
            return False
        target = total // 4
        if max(matchsticks) > target:
            return False
        
        def rec(i, s, sides, used):
            if s > target:
                return False
            if s == target:
                sides += 1
                s = 0
            if i == n:
                return sides == 4
            
            for j in range(n):
                if used[j]:
                    continue
                used[j] = True
                if rec(i + 1, s + matchsticks[j], sides, used):
                    return True
                used[j] = False
            return False
        
        return rec(0, 0, 0, [False] * n)


        # 1,3,4,2,2,4