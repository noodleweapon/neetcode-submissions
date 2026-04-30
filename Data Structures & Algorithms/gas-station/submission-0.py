class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        arr = []
        for g, c in zip(gas, cost):
            arr.append(g - c)
        
        mv = 0
        mi = 0
        for i, elem in enumerate(arr):
            if elem > mv:
                mv = elem
                mi = i
        return mi