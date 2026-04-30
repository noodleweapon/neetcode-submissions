class Solution:
    def rec(self, n, s, words) -> bool:
        if n == len(s):
            return True
        if n > len(s):
            return False

        for word in words:
            if self.rec(n + len(word), s, words):
                return True
        return False


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.rec(0, s, wordDict)