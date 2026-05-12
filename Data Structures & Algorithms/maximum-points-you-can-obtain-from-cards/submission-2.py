class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        M = t = sum(cardPoints[:k])
        for i in reversed(range(k)):
            j = n - k + i
            t -= cardPoints[i]
            t += cardPoints[j]
            M = max(M, t)
        return M