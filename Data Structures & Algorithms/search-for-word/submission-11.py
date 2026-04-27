class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        Y = len(board)
        X = len(board[0])
        def rec(x, y, i, seen_xy):
            if i == len(word):
                return True
            if x < 0 or y < 0:
                return False
            if x >= X or y >= Y:
                return False
            if board[y][x] != word[i]:
                return False
            coord = (x, y)
            if coord in seen_xy:
                return False
            seen_xy.append(coord)
            up = rec(x, y - 1, i + 1, seen_xy)
            down = rec(x, y + 1, i + 1, seen_xy)
            left = rec(x + 1, y, i + 1, seen_xy)
            right = rec(x - 1, y, i + 1, seen_xy)
            seen_xy.pop()
            if up or down or left or right:
                return True

        seen_xy__ = []
        for y in range(Y):
            for x in range(X):
                if rec(x, y, 0, seen_xy__):
                    return True
        
        return False