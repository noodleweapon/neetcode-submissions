class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        N = len(gas)
        s = 0
        tank = 0
        for i in range(N):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                s = i
        return (s + 1) % N