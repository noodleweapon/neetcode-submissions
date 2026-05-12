class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R = len(board)
        C = len(board[0])
        not_surrounded = [[False] * C for _ in range(R)]
        Q = deque([])

        for r in range(R):
            if board[r][0] == 'O':
                Q.append((r, 0))
            if board[r][C - 1] == 'O':
                Q.append((r, C - 1))
        
        for c in range(0, C):
            if board[0][c] == 'O':
                Q.append((0, c))
            if board[R - 1][c] == 'O':
                Q.append((R - 1, c))
        
        while Q:
            (r, c) = Q.popleft()
            not_surrounded[r][c] = True
            for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr
                nc = c + dc
                if nc < 0 or nr < 0 or nc >= C or nr >= R:
                    continue
                if not_surrounded[nr][nc]:
                    continue
                if board[nr][nc] == 'X':
                    continue
                Q.append((nr, nc))
                not_surrounded[nr][nc] = True

        for r in range(R):
            for c in range(C):
                if board[r][c] == 'X':
                    continue
                if not_surrounded[r][c]:
                    continue
                board[r][c] = 'X'




