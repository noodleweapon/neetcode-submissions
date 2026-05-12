class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def has_dup(cs):
            d = {}
            for c in cs:
                if c == '.':
                    continue
                if c in d:
                    return True
                d[c] = 1
            return False

        for r in range(9):
            if has_dup(board[r]):
                return False

        for c in range(9):
            col = list(map(lambda row: row[c], board))
            if has_dup(col):
                return False
        
        for Cx in range(0, 9, 3):
            for Cy in range(0, 9, 3):
                box = []
                for i in range(3):
                    for j in range(3):
                        box.append(board[Cx + i][Cy + j])
                if has_dup(box):
                    return False

        return True