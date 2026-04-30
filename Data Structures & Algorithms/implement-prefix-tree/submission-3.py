class PrefixTree:

    def __init__(self):
        self.d = {}
        self.isEnd = False

    def insert(self, word: str) -> None:
        t = self
        for i, c in enumerate(word):
            if c in t.d:
                t = t.d[c]
            else:
                t.d[c] = PrefixTree()
                t = t.d[c]
        t.isEnd = True

    def search(self, word: str) -> bool:
        t = self
        for i, c in enumerate(word):
            if c in t.d:
                t = t.d[c]
            else:
                t.d[c] = PrefixTree()
                t = t.d[c]
        return t.isEnd

    def startsWith(self, prefix: str) -> bool:
        t = self
        for i, c in enumerate(prefix):
            if c in t.d:
                t = t.d[c]
            else:
                t.d[c] = PrefixTree()
                t = t.d[c]
        return True
    
