class Solution:
    def wordBreak(self, s: str, words: List[str]) -> List[str]:
        def rec(i):
            if i == len(s):
                return ["<>"]
            res = []
            for word in words:
                j = i + len(word)
                if j > len(s):
                    continue
                if s[i:j] != word:
                    continue
                for tail in rec(j):
                    if tail == "<>":
                        res.append(word)
                    else:
                        res.append(word + " " + tail)
            return res
        
        return rec(0)