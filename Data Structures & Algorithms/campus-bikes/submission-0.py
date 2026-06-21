class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        del_i = set()
        del_j = set()

        h = []
        for i, worker in enumerate(workers):
            x, y = worker
            for j, bike in enumerate(bikes):
                bx, by = bike
                dist = abs(x - bx) + abs(y - by)
                heapq.heappush(h, (dist, i, j))

        res = [-1] * len(workers)
        assigned = 0
        while assigned < len(workers):
            dist, i, j = heapq.heappop(h)
            if i in del_i or j in del_j:
                continue
            del_i.add(i)
            del_j.add(j)
            res[i] = j
            assigned += 1
        return res