class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for u in nums:
            l, r = 0, len(dp) # index to insert to.
            if not dp or dp[-1] < u:
                dp.append(u)
                continue
            while l < r:
                m = (l + r) // 2
                if dp[m] >= u:
                    r = m
                else:
                    l = m + 1
            dp[l] = u
        print(dp)
        return len(dp)