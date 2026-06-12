class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        n = len(target)
        def str_to_tup(x):
            return tuple(map(lambda c: int(c), list(x)))

        target = str_to_tup(target)
        start = tuple([0] * n)
        stuck = {str_to_tup(deadend) for deadend in deadends}
        if start in stuck or target in stuck:
            return -1
        if start == target:
            return 0

        q = deque([start])
        stuck.add(start)
        d = 0
        while q:
            for _ in range(len(q)):
                pos = q.popleft()
                if pos == target:
                    return d
                for i in range(n):
                    left = list(pos)
                    right = list(pos)
                    left[i] = (left[i] + 9) % 10
                    right[i] = (right[i] + 1) % 10
                    left = tuple(left)
                    right = tuple(right)
                    if left not in stuck:
                        q.append(left)
                        stuck.add(left)
                    if right not in stuck:
                        q.append(right)
                        stuck.add(right)
            d += 1

        return -1
        # if target in 