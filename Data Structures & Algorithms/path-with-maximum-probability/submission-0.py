class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        g = [[] for _ in range(n)]
        for edge, p in zip(edges, succProb):
            a, b = edge
            g[a].append((b, p))
            g[b].append((a, p))

        prob = [0] * n
        prob[start_node] = 1
        h = [(-1, start_node)]

        while h:
            neg_p, u = heapq.heappop(h)
            up = -neg_p
            if prob[u] > up:
                continue
            prob[u] = up
            
            for (v, edge_p) in g[u]:
                vp = up * edge_p
                if vp <= prob[v]:
                    continue
                heapq.heappush(h, (-vp, v))

        return prob[end_node]