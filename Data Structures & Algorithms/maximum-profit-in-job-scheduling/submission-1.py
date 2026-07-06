class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        D = defaultdict(list)
        for s, e, p in zip(startTime, endTime, profit):
            D[e].append((s, p))

        ends = list(sorted(D))
        n = len(ends)
        P = [0] * n
        def binSearch(start, ind):
            if start < ends[0]:
                return 0
            l, r = 0, ind - 1
            while l < r:
                m = (l + r + 1) // 2
                if ends[m] <= start:
                    l = m
                else:
                    r = m - 1
            return P[l]

        for i in range(n):
            if i > 0:
                P[i] = P[i - 1]
            for s, p in D[ends[i]]:
                include = p + binSearch(s, i)
                P[i] = max(P[i], include)

        return P[n - 1]