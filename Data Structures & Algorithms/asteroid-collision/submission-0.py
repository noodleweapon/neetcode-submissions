class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for v in asteroids:
            s.append(v)
            while len(s) > 1 and s[-2] > 0 and s[-1] < 0:
                b = s.pop()
                a = s.pop()
                if a > -b:
                    s.append(a)
                elif -b > a:
                    s.append(b)
        return s