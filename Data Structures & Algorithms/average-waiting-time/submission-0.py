class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        # 1,2,2,2,2,3
        t = 0
        wait = 0
        for s_i, d_i in customers:
            if t < s_i:
                t = s_i
            wait += t - s_i + d_i
            t += d_i
        return wait / len(customers)

        # t = 11
        # idled = 1
        # 1 + 2 + 5 + 3 = 11
        [1,2],[2,5],[4,3]