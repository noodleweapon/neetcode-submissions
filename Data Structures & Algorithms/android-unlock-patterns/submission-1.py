class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        coords = []
        coord_to_ind = {}
        for r in range(3):
            for c in range(3):
                coord_to_ind[(r, c)] = len(coords)
                coords.append((r, c))
        used = [False] * 9
        cross = [[None] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                a, b = coords[i], coords[j]
                mid = [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2]
                if mid[0] != int(mid[0]) or mid[1] != int(mid[1]):
                    continue
                cross[i][j] = coord_to_ind[(int(mid[0]), int(mid[1]))]

        res = 0
        def rec(stack):
            nonlocal res
            if m <= len(stack) <= n:
                res += 1

            for i in range(9):
                if used[i]:
                    continue
                center = cross[stack[-1]][i] if stack else None
                if center != None and (not used[center]):
                    continue

                used[i] = True
                stack.append(i)
                rec(stack)

                used[i] = False
                stack.pop()
        
        rec([])
        return res

        
