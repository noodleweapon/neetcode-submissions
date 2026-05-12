class UF:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, i):
        if self.par[i] != i:
            self.par[i] = self.find(self.par[i])
        return self.par[i]
    
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
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, edge in enumerate(edges):
            edge.append(i)
        
        edges.sort(key=lambda x: x[2])

        mst_uf = UF(n)
        mst_cost = 0
        for a, b, e_w, _ in edges:
            if mst_uf.union(a, b):
                mst_cost += e_w
        
        critical = []
        pseudo = []
        for i1, i2, e_w, e_i in edges:
            # critical
            cri_uf = UF(n)
            cri_cost = 0
            for (a, b, w, _e_i) in edges:
                if _e_i == e_i:
                    continue
                if cri_uf.union(a, b):
                    cri_cost += w
                
            # print(mst_cost, cri_cost)
            # print(cri_uf.rank)
            
            if cri_cost > mst_cost or max(cri_uf.rank) != n:
                critical.append(e_i)
                continue

            # pseudo
            pse_uf = UF(n)
            pse_cost = e_w
            pse_uf.union(i1, i2)

            for (a, b, w, _) in edges:
                if pse_uf.union(a, b):
                    pse_cost += w
            
            if pse_cost == mst_cost:
                pseudo.append(e_i)

        return [critical, pseudo]