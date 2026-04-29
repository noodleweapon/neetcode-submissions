class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] += 1
        accum = 0
        res = 0
        for num in nums:
            accum += num
            seek = accum - k
            res += d[seek]
            d[accum] += 1
        return res