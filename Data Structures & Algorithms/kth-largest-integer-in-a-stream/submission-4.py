import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = nums
        self.k = k
        heapq.heapify(self.h)

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        return heapq.nlargest(self.k, self.h)[-1]
        
