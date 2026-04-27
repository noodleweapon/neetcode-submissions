class CountSquares:

    def __init__(self):
        self.d = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.d[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0

        for (x2, y2), cnt in self.d.items():
            dx = x2 - x
            dy = y2 - y

            if abs(dx) != abs(dy) or dx == 0:
                continue

            res += cnt * self.d.get((x + dx, y), 0) * self.d.get((x, y + dy), 0)

        return res