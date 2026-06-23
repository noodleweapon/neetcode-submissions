class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        n = 0
        rlist = []
        clist = []
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    continue
                n += 1
                rlist.append(r)
                clist.append(c)
        
        rlist.sort()
        clist.sort()
        
        _r = rlist[n // 2]
        _c = clist[n // 2]

        res = 0
        for r in rlist:
            res += abs(r - _r)
        for c in clist:
            res += abs(c - _c)
        return res



        # 2 / 3 --> 1

        # # mat = [[0] * C for _ in range(R)]