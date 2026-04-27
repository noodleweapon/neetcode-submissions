class PrefixTree:

    def __init__(self):
        self.d = {}

    def insert(self, word: str) -> None:
        t = self.d
        for i, c in enumerate(word):
            if c in t:
                t = t[c].d
            else:
                t[c] = PrefixTree()
                t = t[c].d
        t["#"] = True

    def search(self, word: str) -> bool:
        t = self.d
        for i, c in enumerate(word):
            if c in t:
                t = t[c].d
            else:
                return False
        return t.get("#", False)

    def startsWith(self, prefix: str) -> bool:
        t = self.d
        for i, c in enumerate(prefix):
            if c in t:
                t = t[c].d
            else:
                return False
        return True
    
