class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        par = [i for i in range(n)]
        rank = [1] * n
    
        def find(v):
            if par[v] != v:
                par[v] = find(par[v])
            return par[v]

        def union(a, b):
            A, B = find(a), find(b)
            if A == B:
                return False
            if rank[A] > rank[B]:
                par[B] = A
                rank[A] += rank[B]
            else:
                par[A] = B
                rank[B] += rank[A]
            return True
        
        edges = []
        for i1, p1 in enumerate(points):
            for i2, p2 in enumerate(points):
                if i1 >= i2:
                    continue
                dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                heapq.heappush(edges, (dist, i1, i2))
        
        count = 0
        min_cost = 0
        while edges and count < n - 1:
            (d, i1, i2) = heapq.heappop(edges)
            if not union(i1, i2):
                continue
            min_cost += d
            count += 1
        return min_cost

