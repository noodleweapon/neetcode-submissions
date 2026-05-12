class MedianFinder:

    def __init__(self):
        self.L = [] # max heap
        self.R = [] # min heap
        self.m = None

    def addNum(self, num: int) -> None:
        if self.m == None:
            if not self.L and not self.R:
                self.m = num
                return
            
            a, b = -self.L[0], self.R[0]
            if num < a:
                heapq.heapreplace(self.L, -num)
                self.m = a
            elif num > b:
                heapq.heapreplace(self.R, num)
                self.m = b
            else:
                self.m = num

            return
        
        x, y = sorted([num, self.m])
        self.m = None
        if not self.L and not self.R:
            heapq.heappush(self.L, -x)
            heapq.heappush(self.R, y)
            return
        a, b = -self.L[0], self.R[0]

        if b < x: # a < b < x <= y
            heapq.heappush(self.L, -heapq.heappop(self.R))
            heapq.heappush(self.R, x)
            heapq.heappush(self.R, y)
        elif a > y: # x <= y < a < b
            heapq.heappush(self.R, heapq.heappop(self.L))
            heapq.heappush(self.L, -x)
            heapq.heappush(self.L, -y)
        # elif a <= x and y <= b: # a <= x <= y <= b
        else:
            heapq.heappush(self.L, -x)
            heapq.heappush(self.R, y)

            # x < a < y < b
            # print("ERRR")
        

    def findMedian(self) -> float:
        if self.m != None:
            return self.m
        a, b = -self.L[0], self.R[0]
        return (a + b) / 2