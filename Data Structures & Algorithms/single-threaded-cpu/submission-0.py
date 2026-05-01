class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        new_tasks = []
        for i, task in enumerate(tasks):
            new_tasks.append((task[0], task[1], i))
        tasks = new_tasks
        tasks.sort(key=lambda x: x[0])
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