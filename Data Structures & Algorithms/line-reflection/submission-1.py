class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        d = defaultdict(set)
        for x, y in points:
            d[x].add(y)

        xs = list(sorted(d.keys()))
        n = len(xs)
        if n % 2:
            middle = xs[n // 2]
            if middle * 2 != xs[0] + xs[-1]:
                return False

        for i in range(n // 2):
            j = n - 1 - i
            if d[xs[i]] != d[xs[j]]:
                return False
            if xs[i] - xs[0] != xs[-1] - xs[j]:
                return False

        return True