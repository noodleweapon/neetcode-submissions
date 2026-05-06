class Trie:
    def __init__(self, end):
        self.end = end
        self.d = {}
    
    def search(self, word):
        lengths = []
        t = self
        for i, c in enumerate(word):
            if c not in t.d:
                break
            t = t.d[c]
            if t.end:
                lengths.append(i + 1)
        return lengths
    
    def add(self, word): # ok
        t = self
        for c in word:
            if c not in t.d:
                t.d[c] = Trie(False)
            t = t.d[c]
        t.end = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie(False)
        for word in dictionary:
            trie.add(word)

        def rec(i):
            if i == len(s):
                return 0
            a = 1 + rec(i + 1)
            lengths = trie.search(s[i:])
            for length in lengths:
                a = min(a, rec(i + length))
            return a

        return rec(0)