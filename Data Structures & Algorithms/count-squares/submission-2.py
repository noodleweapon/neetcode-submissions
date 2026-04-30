class CountSquares:

    def __init__(self):
        self.d = {}

    def add(self, point: List[int]) -> None:
        if tuple(point) not in self.d:
            self.d[tuple(point)] = 0
        self.d[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0
        for (a, b), freq in self.d.items():
            side_length = abs(a - x)
            if side_length != abs(b - y):
                continue
            if side_length == 0:
                continue
            O = self.d.get((x, b), 0)
            P = self.d.get((y, a), 0)
            res += O * P * freq
        return res
