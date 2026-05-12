class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n < k:
            return 0

        d_short, d_long = defaultdict(int), defaultdict(int)
        l_long = l_short = u_long = u_short = 0
        res = 0

        for r in range(n):
            c = nums[r]

            d_short[c] += 1
            if d_short[c] == 1:
                u_short += 1
            
            d_long[c] += 1
            if d_long[c] == 1:
                u_long += 1
            
            while u_long > k:
                d_long[nums[l_long]] -= 1
                if d_long[nums[l_long]] == 0:
                    u_long -= 1
                l_long += 1
            
            while u_short > k or (u_short == k and d_short[nums[l_short]] >= 2):
                d_short[nums[l_short]] -= 1
                if d_short[nums[l_short]] == 0:
                    u_short -= 1
                l_short += 1
            
            if u_short == u_long == k:
                res += l_short - l_long + 1
        
        return res

        # 1,2,1,3,4
        # 1,2,2,3,4,4 k=3
