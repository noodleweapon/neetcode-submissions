"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        h = []
        for i in range(len(schedule)):
            if schedule[i]:
                heapq.heappush(h, (schedule[i][0].start, i, 0))
        busy = []
        while h:
            _, i, j = heapq.heappop(h)
            if busy and busy[-1].end >= schedule[i][j].start:
                busy[-1].end = max(busy[-1].end, schedule[i][j].end)
            else:
                busy.append(schedule[i][j])
            if j < len(schedule[i]) - 1:
                heapq.heappush(h, (schedule[i][j + 1].start, i, j + 1))
        res = []
        for i in range(len(busy) - 1):
            a, b = busy[i], busy[i + 1]
            res.append(Interval(a.end, b.start))
        return res


        # h = []
        # qs = [[] for _ in range(len(schedule))]
        # for i, employee in enumerate(schedule):
        #     if not employee:
        #         continue
        #     qs[i] = deque(employee)
        #     heapq.heappush(h, (employee[0].start, i))
        
        # busy = []
        # while h:
        #     _, q_ind = heapq.heappop(h)
        #     interval = qs[q_ind].popleft()
        #     if busy and busy[-1].end >= interval.start:
        #         busy[-1].end = max(busy[-1].end, interval.end)
        #     else:
        #         busy.append(interval)
        #     if qs[q_ind]:
        #         heapq.heappush(h, (qs[q_ind][0].start, q_ind))

        # res = []
        # for i in range(len(busy) - 1):
        #     a, b = busy[i], busy[i + 1]
        #     res.append(Interval(a.end, b.start))
        # return res
