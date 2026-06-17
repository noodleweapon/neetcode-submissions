class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # "hrn","hrf","er","enn","rfnn"
        unique_chars = set()
        d = defaultdict(set)
        for word in words:
            for c in word:
                unique_chars.add(c)

        for i in range(len(words) - 1):
            a, b = words[i], words[i + 1]
            n = min(len(a), len(b))
            for i in range(n):
                if a[i] == b[i]:
                    continue
                d[a[i]].add(b[i])
                break
            if len(a) > len(b) and a.startswith(b):
                return ""


        res = []
        visit = defaultdict(int)
        def dfs(u):
            if visit[u] == 2:
                return False
            if visit[u] == 1:
                return True
            visit[u] = 1
            for v in d[u]:
                if dfs(v):
                    return True

            res.append(u)
            visit[u] = 2
            return False

        for u in unique_chars:
            if dfs(u):
                return ""
        res.reverse()
        return "".join(res)

        # ["abc","bcd","cde"]
        # abc



        # abc
        # abcdef
        #  OR
        # aa
        # ab