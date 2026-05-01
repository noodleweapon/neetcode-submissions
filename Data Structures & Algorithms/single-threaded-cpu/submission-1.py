class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted((start, duration, i) for i, (start, duration) in enumerate(tasks))
        n = len(tasks)
        h, res = [], []
        t = ind = 0 # next index we can enqueue
        while h or (ind < n):
            while ind < n and tasks[ind][0] <= t:
                heapq.heappush(h, (tasks[ind][1], tasks[ind][2]))
                ind += 1
            if h:
                (d, index) = heapq.heappop(h)
                t += d
                res.append(index)
            elif ind < n:
                t = tasks[ind][0]

        return res