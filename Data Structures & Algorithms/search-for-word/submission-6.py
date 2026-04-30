class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for y, row in enumerate(board):
            for x, cell in enumerate(row):
                if self.rec(y, x, 0, [], board, word):
                    return True
        return False
    
    def rec(self, y, x, i, path, board, word):
        if word[i] != board[y][x]:
            return False
        if i == len(word) - 1:
            return True
        path.append((y, x))
        options = self.getOptions(y, x, path, board)
        for option in options:
            _y, _x = option
            if self.rec(_y, _x, i + 1, path, board, word):
                return True
        return False

    def getOptions(self, y, x, path, board):
        Y = len(board)
        X = len(board[0])
        options = []
        if x >= 1:
            options.append((y, x - 1))
        if x < X - 1:
            options.append((y, x + 1))
        if y >= 1:
            options.append((y - 1, x))
        if y < Y - 1:
            options.append((y + 1, x))
        return list(filter(lambda a : a not in path, options))
