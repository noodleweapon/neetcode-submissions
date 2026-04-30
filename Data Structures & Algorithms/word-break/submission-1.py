class Solution:
    def rec(self, n, s, words) -> bool:
        if n == len(s):
            return True

        for word in words:
            if n + len(word) > len(s):
                continue
            if s[n:n + len(word)] != word:
                continue
            if self.rec(n + len(word), s, words):
                return True
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.rec(0, s, wordDict)