class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        res = 1
        l = 0
        d = defaultdict(int)
        d[fruits[l]] = 1
        for r in range(1, n):
            d[fruits[r]] += 1
            if len(d) > 2: # both if and while work.
                d[fruits[l]] -= 1
                if d[fruits[l]] == 0:
                    d.pop(fruits[l])
                l += 1
            res = max(res, r - l + 1)
        return res