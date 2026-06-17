class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        t = 0
        wait = 0
        for s_i, d_i in customers:
            if t < s_i:
                t = s_i
            wait += t - s_i + d_i
            t += d_i
        return wait / len(customers)
