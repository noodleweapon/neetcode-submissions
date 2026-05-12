class UF:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, v):
        if self.par[v] != v:
            self.par[v] = self.find(self.par[v])
        return self.par[v]

    def union(self, i1, i2):
        p1, p2 = self.find(i1), self.find(i2)
        if p1 == p2:
            return False
        if self.rank[p1] >= self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        # undirected graph, bec gcd goes both ways.
        # n-1 checks cause order's transitive.
        nums.sort()

        def conn(a, b): # big, small
            if a % 2 == 0 and b % 2 == 0:
                return True
            if a == b + 1:
                return False
            def gcd(a, b): # a is bigger or eq.
                if b == 0:
                    return a
                return gcd(b, a % b)
            
            return gcd(a, b) > 2


        n = len(nums)
        uf = UF(n)
        for i in range(n):
            for j in range(i + 1, n):
                if conn(nums[j], nums[i]):
                    uf.union(i, j)
        
        return max(uf.rank) == n

