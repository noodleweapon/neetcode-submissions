class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # if goal == 0:
        #     res = 0
        #     length = 0
        #     for num in nums:
        #         if num == 1:
        #             length = 0
        #             continue
        #         length += 1
        #         res += length
        #     return res

        #     [1,0,1,0,1]
        #   [0,1,1,2,2,3]
        d = defaultdict(int)
        d[0] += 1
        res = accum = 0
        for num in nums:
            accum += num
            res += d[accum - goal]
            d[accum] += 1
        return res
