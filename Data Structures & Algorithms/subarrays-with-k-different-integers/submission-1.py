class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def at_most_k(f):
            l = freq = 0
            d = defaultdict(int)
            res = 0
            for r in range(n):
                d[nums[r]] += 1
                if d[nums[r]] == 1:
                    freq += 1
                while freq > f:
                    d[nums[l]] -= 1
                    if d[nums[l]] == 0:
                        freq -= 1
                    l += 1
                res += r - l + 1
            return res
        
        return at_most_k(k) - at_most_k(k - 1)