class WordDictionary:

    def __init__(self):
        self.d = {}
        self.f = False

    def addWord(self, word: str) -> None:
        t = self
        for i, c in enumerate(word):
            if c not in t.d:
                t.d[c] = WordDictionary()
            t = t.d[c]
        t.f = True

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self.f
        c = word[0]
        if c == '.':
            for q in self.d.values():
                if q.search(word[1:]):
                    return True
            return False
        else:
            if c not in self.d:
                return False
            return self.d[c].search(word[1:])