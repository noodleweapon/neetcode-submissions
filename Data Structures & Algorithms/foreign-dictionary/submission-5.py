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
            if i == I and l1 <= l2:
                return True
            return False
        
        for i in range(len(words) - 1):
            if not pairwise_compare(words[i], words[i + 1]):
                return ""
        
        alphabet = set()
        for word in words:
            for c in word:
                alphabet.add(c)

        visited = defaultdict(int)
        output = []

        def dfs_cycle(c):
            if visited[c] == 2:
                return False
            if visited[c] == 1:
                return True
            visited[c] = 1
            for nxt in adj[c]:
                if dfs_cycle(nxt):
                    return True
            output.append(c)
            visited[c] = 2
            return False

        for c in alphabet:
            if dfs_cycle(c):
                return ""

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
