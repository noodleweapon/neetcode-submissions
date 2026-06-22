class Trie:
    def __init__(self):
        self.d = {}
        self.f = 0
    
    def record(self, text, f):
        t = self
        for c in text:
            if c not in t.d:
                t.d[c] = Trie()
            t = t.d[c]
        t.f += f

    def getTop3(self, text):
        t = self
        for c in text:
            if c not in t.d:
                return []
            t = t.d[c]
        
        def dfs(s):
            res = []
            if s.f > 0:
                res.append((-s.f, '')) # HAD TO STORE AS "" NOT <END>
            for c in s.d:
                tails = dfs(s.d[c])
                for f2, tail in tails:
                    if tail == '':
                        res.append((f2, c))
                    else:
                        res.append((f2, c + tail))
            return res

        h = dfs(t)
        heapq.heapify(h)
        return list(map(lambda x: text + x[1], heapq.nsmallest(3, h)))

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = Trie()
        self.buffer = ''
        for sentence, f in zip(sentences, times):
            self.root.record(sentence, f)

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.root.record(self.buffer, 1)
            self.buffer = ''
            return []
        else:
            self.buffer += c
            return self.root.getTop3(self.buffer)





# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
