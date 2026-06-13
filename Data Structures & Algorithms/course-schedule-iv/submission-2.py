class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        path = [[False] * n for _ in range(n)]
        for bef, aft in prerequisites:
            path[bef][aft] = True
        
        for i in range(n):
            for k in range(n):
                for j in range(n):
                    path[i][j] = path[i][j] or (path[i][k] and path[k][j])
        
        res = []
        for bef, aft in queries:
            res.append(path[bef][aft])
        return res