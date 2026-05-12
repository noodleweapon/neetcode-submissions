class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        def get_furthest(start):
            def dfs(u, p):
                maxD = (u, [u])
                for v in g[u]:
                    if v == p:
                        continue
                    node, path = dfs(v, u)
                    path.append(u)
                    if len(path) > len(maxD[1]):
                        maxD = (node, path)
                return maxD
            return dfs(start, -1)
        
        node1, _ = get_furthest(0)
        node2, path = get_furthest(node1)
        l, r = 0, len(path) - 1
        while l + 1 <= r - 1:
            l += 1
            r -= 1
        
        return path[l:r+1]