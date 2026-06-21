class UF:
    def __init__(self, n):
        self.size = [1] * n # MISTAKE 2: I had 0 here.
        self.par = [i for i in range(n)]

    def find(self, x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, a, b):
        A, B = self.find(a), self.find(b)
        if A == B:
            return False
        if self.size[A] > self.size[B]:
            self.par[B] = A
            self.size[A] += self.size[B]
        else:
            self.par[A] = B
            self.size[B] += self.size[A]
        
        return True

class Solution:
    def numIslands2(self, R: int, C: int, positions: List[List[int]]) -> List[int]:
        # MISTAKE 1: m x n means m = R, n = C, not the other way.
        n = len(positions)
        to_ind = {}
        uf = UF(n)
        islands = 0
        res = []
        for i, position in enumerate(positions):
            r, c = position
            if (r, c) in to_ind: # MISTAKE 3: Didn't handle duplicates.
                res.append(islands)
                continue
            to_ind[(r, c)] = i
            islands += 1
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if (0 <= nr < R) and (0 <= nc < C) and (nr, nc) in to_ind:
                    if uf.union(i, to_ind[(nr, nc)]):
                        islands -= 1

            res.append(islands)
        return res


            
            
        #     if len(touching_scc) == 0:
        #         islands += 1
        #         scc += 1
        #         grid[r][c] = scc
        #     else:
        #         islands -= len(touching_scc) - 1
        #         min_scc = min(list(touching_scc))
        #         grid[r][c] = 
        #     res.append(islands)
        # return res
