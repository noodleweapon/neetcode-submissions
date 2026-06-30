class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        n, s = len(source), set(source)
        next = [defaultdict(int) for _ in range(n)]
        for i in range(n):
            for c in s:
                pos = source.find(c, i)
                if pos == -1:
                    pos = source.find(c)
                    next[i][c] = n + (pos - i)
                else:
                    next[i][c] = pos - i

        j = 0
        for i in range(len(target)):
            if target[i] not in s:
                return -1
            j += next[j % n][target[i]] + 1 # Still don't fully understand.
        return math.ceil(j / n)