class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        res = types = 1
        l = 0
        d = defaultdict(int)
        d[fruits[l]] = 1
        for r in range(1, n):
            if d[fruits[r]] == 0:
                types += 1
            d[fruits[r]] += 1
            if types > 2: # both if and while work.
                d[fruits[l]] -= 1
                if d[fruits[l]] == 0:
                    types -= 1
                    d.pop(fruits[l])
                l += 1
            res = max(res, r - l + 1)
        return res