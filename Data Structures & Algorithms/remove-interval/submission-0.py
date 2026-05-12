class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        r1, r2 = toBeRemoved
        res = []
        for a1, a2 in intervals:
            if a1 > r2 or a2 < r1: # no overlap
                res.append([a1, a2])
                continue
            left = r1 <= a1
            right = a2 <= r2
            
            if left and right: # r1 <= a1, a2 <= r2
                continue
            
            if (not left) and (not right): # a1 < r1, r2 < a2
                res.append([a1, r1])
                res.append([r2, a2])
                continue
            if left: # r1 <= a1, r2 < a2
                res.append([r2, a2])
            elif right: # a1 < r1, a2 <= r2
                res.append([a1, r1])
        
        return res
