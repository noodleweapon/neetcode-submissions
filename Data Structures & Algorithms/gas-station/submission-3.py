class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        diff = [g - c for g, c in zip(gas, cost)]
        q = deque()
        i = 0
        s = 0
        while len(q) < N:
            ind = (i + 1) % N
            q.append(diff[ind])
            s += diff[ind]
            i += 1

            while s < 0:
                s -= q.popleft()
            if i > 2 * N:
                return -1
        return (i + 1) % N