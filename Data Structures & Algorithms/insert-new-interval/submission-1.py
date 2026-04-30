class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def overlaps(a, b):
            if a[1] < b[0]:
                return False
            if b[1] < a[0]:
                return False
            return True
        
        res = []
        for interval in intervals:
            if not overlaps(interval, newInterval):
                res.append(interval)
                continue
            newInterval[0] = min(newInterval[0], interval[0])
            newInterval[1] = max(newInterval[1], interval[1])
        
        insert_at = 0
        for i in range(len(res)):
            if newInterval[0] < res[i][0]:
                insert_at = i
                break
        res.insert(insert_at, newInterval)
        return res
