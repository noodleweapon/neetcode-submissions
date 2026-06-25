class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        s = []
        for num in nums:
            l, r = 0, len(s)
            while l < r:
                m = (l + r + 1) // 2
                cond = s[m - 1] < num if m > 0 else True
                if cond:
                    l = m
                else:
                    r = m - 1
            if l == len(s):
                s.append(num)
            else:
                s[l] = num
        return len(s)

        # 0,1,0,3,2,3
        # 0,1,2,3

        # 1,3,5,2,4
        # 1,2,4,

        # 9,1,4,2,3,3,7