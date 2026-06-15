class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        points = list(map(tuple, points))
        members = set(points)
        min_x = min(map(lambda point: point[0], points))
        max_x = max(map(lambda point: point[0], points))
        const = min_x + max_x
        for x, y in points:
            if (const - x, y) not in members:
                return False
        return True
