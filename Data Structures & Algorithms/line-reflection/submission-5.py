class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        points = set(map(tuple, points))
        min_x = min([x for x, y in points])
        max_x = max([x for x, y in points])
        const = min_x + max_x
        for x, y in points:
            if (const - x, y) not in points:
                return False
        return True
