class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n, total = len(matchsticks), sum(matchsticks)
        if total % 4 != 0:
            return False
        target = total // 4
        matchsticks.sort(reverse=True)
        if matchsticks[0] > target:
            return False
        seen = set()
        def rec(i, buckets):
            if (i, *sorted(buckets)) in seen:
                return False
            if i == n:
                return min(buckets) == max(buckets) == target
            for j in range(4):
                if j > 0 and buckets[j - 1] == 0:
                    continue
                if buckets[j] + matchsticks[i] > target:
                    continue
                buckets[j] += matchsticks[i]
                if rec(i + 1, buckets):
                    return True
                buckets[j] -= matchsticks[i]
            seen.add((i, *sorted(buckets)))
            return False
        return rec(0, [0,0,0,0])

        6,6,6,5,4,4,3,2
        [], [], [], []


        # 1,3,4,2,2,4