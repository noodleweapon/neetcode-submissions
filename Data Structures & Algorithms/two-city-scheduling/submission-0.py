class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        aPref = [a - b for a, b in costs]
        aPref.sort(reverse=False)
        res = sum(aPref[:n])
        res += sum([b for _, b in costs])
        return res