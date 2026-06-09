class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort(key=lambda x: x[0]) # s, d, i

        h, res = [], []
        task_i = time = 0
        while h or task_i < len(tasks):
            while task_i < len(tasks) and tasks[task_i][0] <= time:
                s, d, i = tasks[task_i]
                heapq.heappush(h, (d, i))
                task_i += 1
            if h:
                d, i = heapq.heappop(h)
                time += d
                res.append(i)
            elif task_i < len(tasks):
                time = tasks[task_i][0]
            
        return res
