class Trie:
    def __init__(self):
        self.d = {}
        self.l = 0
    
    def add(self, text):
        l = len(text)
        node = self
        for c in text:
            if c not in node.d:
                node.d[c] = Trie()
            node = node.d[c]
        node.l = l

    def get_matching_lengths(self, text):
        node = self
        res = []
        for c in text:
            if c not in node.d:
                break
            node = node.d[c]
            if node.l > 0:
                res.append(node.l)
        return res

class Solution:
    def minExtraChar(self, s: str, words: List[str]) -> int:
        t = Trie()
        for word in words:
            t.add(word)
        
        dp = {}

        def rec(i):
            if i in dp:
                return dp[i]
            if i == len(s):
                return 0
            ls = t.get_matching_lengths(s[i:len(s)])
            M = rec(i + 1) + 1
            for l in ls:
                M = min(M, rec(i + l))
            dp[i] = M
            return M

        return rec(0)
