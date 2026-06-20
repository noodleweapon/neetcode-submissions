class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        E = [set() for _ in range(n)]
        for u, v in edges:
            E[u].add(v)
            E[v].add(u)
        
        def get_furthest(start):
            a_dist = 0
            a_node = start
            def dfs1(u, prev, dist):
                nonlocal a_node, a_dist

                if dist > a_dist:
                    a_dist = dist
                    a_node = u

                for v in E[u]:
                    if v == prev:
                        continue
                    dfs1(v, u, dist + 1)

            dfs1(start, None, 0)
            return (a_node, a_dist)
        
        a, _ = get_furthest(0)
        _, d = get_furthest(a)
        return d
        