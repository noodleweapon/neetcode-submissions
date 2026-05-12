class UF:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, v):
        if self.par[v] != v:
            self.par[v] = self.find(self.par[v])
        return self.par[v]

    def union(self, p1, p2):
        if self.rank[p1] >= self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        # undirected graph, bec gcd goes both ways.
        # n-1 checks cause order's transitive.

        def gcd(a, b): # a is bigger or eq.
            if b == 0:
                return a
            return gcd(b, a % b)

        n = len(nums)
        uf = UF(n)
        for i in range(n):
            for j in range(i + 1, n):
                p1, p2 = uf.find(i), uf.find(j)
                if p1 == p2:
                    continue
                a, b = max(nums[j], nums[i]), min(nums[j], nums[i])
                if gcd(a, b) > 1:
                    uf.union(p1, p2)
        
        return max(uf.rank) == n

