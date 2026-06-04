class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort(reverse=True)
        s = set(nums)
        M = 1
        for num in nums:
            if num not in s:
                continue
            s.remove(num)
            o = 1
            while num - o in s:
                s.remove(num - o)
                o += 1
            M = max(M, o)
        return M
# 1,2,3