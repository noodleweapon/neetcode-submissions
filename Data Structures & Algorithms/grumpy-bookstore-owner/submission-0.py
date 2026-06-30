class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        res = sum([customers[i] if not grumpy[i] else 0 for i in range(n)])


        for i in range(n):
            if not grumpy[i]:
                customers[i] = 0
        S = M = sum(customers[:minutes])
        for r in range(minutes, n):
            l = r - minutes
            S += customers[r] - customers[l]
            M = max(M, S)
        return res + M