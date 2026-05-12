class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        s = 0
        t = 0
        for i in range(n):
            t += gas[i] - cost[i]
            if t < 0:
                t = 0
                s = i + 1
                continue
        return s % n