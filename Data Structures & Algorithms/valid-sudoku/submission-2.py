class Solution:
    def hasDup(self, nums):
        nums = list(filter(lambda x: x == ".", nums))
        return len(set(nums)) != len(nums)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if self.hasDup(row):
                return False
            
        for c in range(0, 9):
            col = [row[c] for row in board]
            if self.hasDup(col):
                return False
        
        cxy = []
        for x in [1, 4, 7]:
            for y in [1, 4, 7]:
                cxy.append([x, y])

        for cx, cy in cxy:
            nums = []
            for x in [-1, 0, -1]:
                for y in [-1, 0, -1]:
                    nums.append(board[cx + x][cy + y])

            if self.hasDup(nums):
                return False

        return True

