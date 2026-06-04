class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        p = res = 0
        for num in nums:
            p += num
            res += d[p - k]
            d[p] += 1
        return res
        