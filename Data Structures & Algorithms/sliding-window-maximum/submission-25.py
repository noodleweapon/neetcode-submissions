class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 1,2,1,0,4,2,6
        # monotonic queue. q[0] is biggest. store ind too.
        # STACK WITH A FALLING BOTTOM.
        n = len(nums)
        q = deque([])
        res = []
        for i in range(n):
            print(q)
            while q and nums[q[-1]] <= nums[i]: # STACK
                q.pop()
            while q and i - q[0] >= k: # FALLING BOTTOM
                q.popleft()
            q.append(i)
            if i >= k - 1:
                res.append(nums[q[0]])
        return res
