class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ls = set(map(len, wordDict))

        def dfs(i):
            if i == len(s):
                return ["<FIN>"]
            res = []
            for l in ls:
                j = i + l
                word = s[i:j]
                if word not in wordDict:
                    continue
                for tail in dfs(j):
                    if tail == "<FIN>":
                        res.append(word)
                    else:
                        res.append(word + " " + tail)
            return res

        return dfs(0)