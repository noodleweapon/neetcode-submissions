class UF:
    def __init__(self):
        self.parent = {}
        self.synonyms = defaultdict(set)
    
    def add(self, x):
        if x in self.parent:
            return
        self.parent[x] = x
        self.synonyms[x].add(x)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        A, B = self.find(a), self.find(b)
        if A == B:
            return False
        
        if len(self.synonyms[A]) > len(self.synonyms[B]):
            self.parent[B] = A
            self.synonyms[A].update(self.synonyms[B])
            self.synonyms[B] = set()
        else:
            self.parent[A] = B
            self.synonyms[B].update(self.synonyms[A])
            self.synonyms[A] = set()
        
        return True

class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        uf = UF()
        for a, b in synonyms:
            uf.add(a)
            uf.add(b)
            uf.union(a, b)

        words = text.split(" ")

        def dfs(i):
            if i == len(words):
                return ['<END>']
            word = words[i]
            if word in uf.parent:
                synonyms = uf.synonyms[uf.find(word)]
            else:
                synonyms = [word]
                
            res = []
            for synonym in synonyms:
                tails = dfs(i + 1)
                for tail in tails:
                    if tail == '<END>':
                        res.append(synonym)
                    else:
                        res.append(synonym + ' ' + tail)
            return res

        return list(sorted(dfs(0)))