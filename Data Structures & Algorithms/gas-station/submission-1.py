class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        arr = []
        for g, c in zip(gas, cost):
            arr.append(g - c)
        
        res = 0
        total = 0
        for i in range(len(arr)):
            total += arr[i]
            if total < 0:
                total = 0
                res = i + 1
        return res

