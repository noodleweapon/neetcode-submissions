class MedianFinder:

    def __init__(self):
        self.L = [] # 5,3,2,1
        self.R = [] # 7,6 9,10

    def addNum(self, num: int) -> None:
        heapq.heappush(self.L, -num)
        if len(self.L) == len(self.R) + 2:
            val = -1 * heapq.heappop(self.L)
            heapq.heappush(self.R, val)

        if self.L and self.R and -self.L[0] > self.R[0]:
            l = -heapq.heappop(self.L)
            r = heapq.heappop(self.R)
            heapq.heappush(self.L, -r)
            heapq.heappush(self.R, l)

    def findMedian(self) -> float:
        if not self.L:
            return 0
        if len(self.L) != len(self.R):
            return -1 * self.L[0]
        return (self.R[0] - self.L[0]) / 2
