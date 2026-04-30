class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        ALL = "abcdefgjijklmnopqrstuv"
        adj = defaultdict(set)

        def pairwise_compare(w1, w2):
            l1, l2 = len(w1), len(w2)
            I = min(l1, l2)
            i = 0
            while i < I:
                c1, c2 = w1[i], w2[i]
                if c1 != c2:
                    adj[c1].add(c2)
                    return True
                i += 1
            if i == I and l1 < l2:
                return True
            return False
        
        alphabet = set()
        for i in range(len(words) - 1):
            for c in words[i]:
                alphabet.add(c)
            if not pairwise_compare(words[i], words[i + 1]):
                return ""
        
        visited = defaultdict(bool)
        output = []
        def dfs(c):
            if visited[c]:
                return
            visited[c] = True
            for nxt in adj[c]:
                dfs(nxt)
            output.append(c)

        for c in alphabet:
            dfs(c)

        output.reverse()
        return "".join(output)

        # hheer
        # h --> e
        # e --> r
        # rrrnf
        # r --> n
        # n --> f
        # nfnn # don't care, not first diff.
        # n --> f
        # f --> n
