class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        def get_furthest(start):
            def dfs(u, p):
                maxD = [u]
                for v in g[u]:
                    if v == p:
                        continue
                    path = dfs(v, u)
                    path.append(u)
                    if len(path) > len(maxD):
                        maxD = path
                return maxD
            return dfs(start, -1)
        
        path1 = get_furthest(0)
        path2 = get_furthest(path1[0])
        l, r = 0, len(path2) - 1
        while l + 1 <= r - 1:
            l += 1
            r -= 1
        
        return path2[l:r+1]