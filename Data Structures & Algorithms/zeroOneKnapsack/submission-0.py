class Solution:
    def rec(self, i, ps, ws, cap):
        if i == len(ps):
            return 0

        p1 = self.rec(i + 1, ps, ws, cap)
        p2 = ps[i] + self.rec(i + 1, ps, ws, cap - ws[i]) if ws[i] <= cap else 0
        return max(p1, p2)

    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        return self.rec(0, profit, weight, capacity)
