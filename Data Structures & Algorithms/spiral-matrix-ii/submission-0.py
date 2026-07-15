class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[0] * n for _ in range(n)]
        top = left = 0
        bot = right = n - 1
        z = 0
        side = 0
        while left <= right and top <= bot:
            if side == 0:
                for c in range(left, right + 1):
                    z += 1
                    grid[top][c] = z
                top += 1
            elif side == 1:
                for r in range(top, bot + 1):
                    z += 1
                    grid[r][right] = z
                right -= 1
            elif side == 2:
                for c in reversed(range(left, right + 1)):
                    z += 1
                    grid[bot][c] = z
                bot -= 1
            elif side == 3:
                for r in reversed(range(top, bot + 1)):
                    z += 1
                    grid[r][left] = z
                left += 1

            side += 1
            side %= 4
        return grid