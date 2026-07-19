class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        # need to serialize them in some way
        # perimeter idea. - unclear bec of inner ponds.
        # 2 DFS idea?
        # quadrant idea: Make one quadrant the heaviest one.
        # allow flipping as well.
        # I HAD TO TRY ALL 8 cases!!

        def transform(_arr, xySwap, xFlip, yFlip):
            maxR = max([r for r, _ in _arr])
            maxC = max([c for _, c in _arr])
            arr = []
            for i in range(len(_arr)):
                r, c = _arr[i]
                if xFlip:
                    c = maxC - c
                if yFlip:
                    r = maxR - r
                elem = [c, r] if xySwap else [r, c]
                arr.append(elem)
            arr.sort()
            return arr

    
        def serialize(arr):
            minR = min([r for r, _ in arr])
            minC = min([c for _, c in arr])
            m = len(arr)
            for i in range(m):
                arr[i][0] -= minR
                arr[i][1] -= minC
            
            options = []
            for xySwap in [True, False]:
                for xFlip in [True, False]:
                    for yFlip in [True, False]:
                        options.append(tuple(map(tuple, transform(arr, xySwap, xFlip, yFlip))))

            return min(options)

        def dfs(r, c, arr):
            grid[r][c] = 0
            arr.append([r, c])
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if not (0 <= nr < R and 0 <= nc < C):
                    continue
                if grid[nr][nc] == 1:
                    dfs(nr, nc, arr)

        S = set()
        R, C = len(grid), len(grid[0])
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    continue
                arr = []
                dfs(r, c, arr)
                S.add(serialize(arr))
        
        return len(S)