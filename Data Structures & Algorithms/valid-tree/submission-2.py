class UF:
    def __init__(self, n):
        self.rank = [1] * n
        self.par = [i for i in range(n)]
    
    def find(self, i):
        if self.par[i] != i:
            self.par[i] = self.find(self.par[i])
        return self.par[i]
    
    def union(self, a, b):
        A, B = self.find(a), self.find(b)
        if A == B:
            return False
        if self.rank[A] < self.rank[B]:
            self.rank[B] += self.rank[A]
            self.par[A] = B
        else:
            self.rank[A] += self.rank[B]
            self.par[B] = A
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UF(n)
        for a, b in edges:
            if not uf.union(a, b):
                return False
        
        print(uf.rank)
        return max(uf.rank) == n
        


