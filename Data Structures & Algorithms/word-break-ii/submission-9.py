class Solution:
    def wordBreak(self, s: str, words: List[str]) -> List[str]:
        words = set(words)
        ls = set(map(len, words))
        dp = {}
        def rec(i):
            if i in dp:
                return dp[i]
            if i == len(s):
                return ["<>"]
            res = []
            for l in ls:
                j = i + l
                if j > len(s):
                    continue
                word = s[i:j]
                if word not in words:
                    continue
                for tail in rec(j):
                    if tail == "<>":
                        res.append(word)
                    else:
                        res.append(word + " " + tail)

            dp[i] = res
            return res
        
        return rec(0)