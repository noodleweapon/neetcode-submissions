class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        diff = [g - c for g, c in zip(gas, cost)]
        s = 0
        tank = 0
        for i in range(N):
            tank += diff[i]
            if tank < 0:
                tank = 0
                s = i
        return s