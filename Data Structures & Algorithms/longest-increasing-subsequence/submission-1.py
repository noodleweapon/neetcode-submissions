class Solution:
    def rec(self, i, cur, nums):
        if i == len(nums):
            return len(cur)
        
        a = self.rec(i + 1, cur, nums)

        if cur == [] or nums[i] > cur[-1]:
            cur.append(nums[i])
            b = self.rec(i + 1, cur, nums)
            a = max(a, b)
            cur.pop()
        return a

    def lengthOfLIS(self, nums: List[int]) -> int:
        cur = []
        return self.rec(0, cur, nums)