class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        Y = len(board)
        X = len(board[0])
        def rec(x, y, i):
            if i == len(word):
                return True
            if x < 0 or y < 0:
                return False
            if x >= X or y >= Y:
                return False
            if board[y][x] != word[i]:
                return False
            up = rec(x, y - 1, i + 1)
            down = rec(x, y + 1, i + 1)
            left = rec(x + 1, y, i + 1)
            right = rec(x - 1, y, i + 1)
            if up or down or left or right:
                return True

        for y in range(Y):
            for x in range(X):
                if rec(x, y, 0):
                    return True
        
        return False