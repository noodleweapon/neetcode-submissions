import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        add_heap = []
        sub_heap = []
        out = []

        l = r = 0
        while r < len(nums):
            heapq.heappush(add_heap, -nums[r])
            r += 1
            if r >= k:
                out.append(-add_heap[0])

            if r - l > k:
                heapq.heappush(sub_heap, -nums[l])
                l += 1
            
            while add_heap and sub_heap and add_heap[0] == sub_heap[0]:
                heapq.heappop(add_heap)
                heapq.heappop(sub_heap)
        
        return out