class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        p = res = 0
        for num in nums:
            p += num
            d[p] += 1
            res += d[p - k]
            if k == 0:
                res -= 1
        return res
        