class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        M = 1
        for num in nums:
            if num - 1 in s:
                continue
            o = 1
            while num + o in s:
                o += 1
            M = max(M, o)
        return M
