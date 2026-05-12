class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        def dfs(i, words):
            if i == len(s):
                res.append(" ".join(words))
                return

            for w, word in enumerate(wordDict):
                j = i + len(word)
                if j > len(s):
                    continue
                if s[i:j] != word:
                    continue
                words.append(word)
                dfs(j, words)
                words.pop()

        dfs(0, [])
        return res