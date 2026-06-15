class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        points = list(map(tuple, points))
        members = set(points)
        min_x = min(x for x, y in points)
        max_x = max(x for x, y in points)
        const = min_x + max_x
        for x, y in points:
            if (const - x, y) not in members:
                return False
        return True
