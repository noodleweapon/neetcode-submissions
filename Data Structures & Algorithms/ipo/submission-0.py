class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits) #
        pc = [(p, c) for p, c in zip(profits, capital)] #
        pc.sort(key=lambda x: x[1]) #
        q = deque(pc) #

        h = [] #
        take = 0
        while h or q: #
            while q and q[0][1] <= w: #
                heapq.heappush(h, -1 * q.popleft()[0]) #
            if not h: # 
                break #
            delta = -1 * heapq.heappop(h) #
            w += delta
            take += 1
            if take == k:
                break

        return w