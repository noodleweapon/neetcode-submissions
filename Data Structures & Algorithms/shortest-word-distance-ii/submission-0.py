class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.d = defaultdict(list)
        for i in range(len(wordsDict)):
            self.d[wordsDict[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        A, B = self.d[word1], self.d[word2]
        i, j = 0, 0
        res = float("inf")
        while i < len(A) and j < len(B):
            res = min(res, abs(A[i] - B[j]))
            if A[i] <= B[j]:
                i += 1
            else:
                j += 1
        return res


        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
