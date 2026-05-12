class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        for i, n in enumerate(nums):
            nxt = defaultdict(int)
            for s, f in dp.items():
                nxt[s + n] += f
                nxt[s - n] += f
            dp = nxt
        return dp.get(target, 0)