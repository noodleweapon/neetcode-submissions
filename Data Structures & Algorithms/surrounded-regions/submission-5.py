class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R = len(board)
        C = len(board[0])
        not_surrounded = [[False] * C for _ in range(R)]
        Q = deque([])

        def add(r, c):
            if board[r][c] == 'X':
                return
            if not_surrounded[r][c]:
                return
            Q.append((r, c))
            not_surrounded[r][c] = True

        for r in range(R):
            add(r, 0)
            add(r, C - 1)
        
        for c in range(0, C):
            add(0, c)
            add(R - 1, c)
        
        while Q:
            (r, c) = Q.popleft()
            not_surrounded[r][c] = True
            for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr
                nc = c + dc
                if nc < 0 or nr < 0 or nc >= C or nr >= R:
                    continue
                add(nr, nc)

        for r in range(R):
            for c in range(C):
                if board[r][c] == 'X':
                    continue
                if not_surrounded[r][c]:
                    continue
                board[r][c] = 'X'




