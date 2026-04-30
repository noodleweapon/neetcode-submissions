import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        ms = []
        for i in range(k):
            num = nums[i]
            heapq.heappush(h, (-num, i))

        for i in range(k - 1, len(nums)):
            num = nums[i]
            heapq.heappush(h, (-num, i))
            while h and h[0][1] < i - k - 1:
                heapq.heappop(h)
            ms.append(h[0])
        
        return list(map(lambda x: -x[0], ms))