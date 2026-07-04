class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        d1, d7, d30 = costs
        n = len(days)
        numDays = max(days)
        dp = [float("inf")] * (numDays + 1)
        daysSet = set(days)
        dp[0] = 0
        def dpGet(d):
            if d >= 0:
                return dp[d]
            else:
                return dp[0]
        for day in range(1, numDays + 1):
            if day not in daysSet:
                dp[day] = dpGet(day - 1)
                continue
            dp[day] = min(dp[day], dpGet(day - 1) + d1)
            dp[day] = min(dp[day], dpGet(day - 7) + d7)
            dp[day] = min(dp[day], dpGet(day - 30) + d30)
        return dp[numDays]
