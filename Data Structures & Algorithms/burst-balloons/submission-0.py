class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        popped = [False] * n

        def get_l(ind):
            for i in reversed(range(0, ind)):
                if not popped[i]:
                    return i
            return -1

        def get_r(ind):
            for i in range(ind, n):
                if not popped[i]:
                    return i
            return -1

        def rec(pops):
            if pops == n:
                return 0
            
            for i in range(n):
                l = get_l(i)
                r = get_r(i)
                L = 1 if l == -1 else nums[l]
                rec(pops + 1)

    
        return rec(0)