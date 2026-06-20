# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        ships = 0
        q = deque([(bottomLeft, topRight)])

        while q and ships < 10:
            a, b = q.popleft()
            if not sea.hasShips(b, a):
                continue
            if (b.y == a.y) and (b.x == a.x):
                ships += 1
                continue
            if b.y - a.y > b.x - a.x:
                my1 = (a.y + b.y) // 2
                my2 = my1 + 1
                a1, b1 = a, Point(b.x, my1)
                a2, b2 = Point(a.x, my2), b
            else:
                mx1 = (a.x + b.x) // 2
                mx2 = mx1 + 1
                a1, b1 = a, Point(mx1, b.y)
                a2, b2 = Point(mx2, a.y), b
            q.append((a1, b1))
            q.append((a2, b2))

        return ships