class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        n, s = len(source), set(source)
        j = 0
        for i in range(len(target)):
            if target[i] not in s:
                return -1
            while target[i] != source[j % n]:
                j += 1
            j += 1
        return math.ceil(j / n)