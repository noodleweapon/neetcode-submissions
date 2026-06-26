class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        ls = list(set([len(word) for word in words]))
        ls.sort(reverse=True)
        words = set(words)
        bold = [False] * len(s)
        for i in range(len(s)):
            for l in ls:
                if i+l > len(s):
                    continue
                if s[i:i+l] not in words:
                    continue
                for j in range(i, i + l):
                    bold[j] = True
                break
        prev = False
        res = ""
        for i in range(len(s)):
            if not prev and bold[i]:
                res += "<b>"
            elif prev and not bold[i]:
                res += "</b>"
            res += s[i]
            prev = bold[i]
        if prev:
            res += "</b>"
        return res