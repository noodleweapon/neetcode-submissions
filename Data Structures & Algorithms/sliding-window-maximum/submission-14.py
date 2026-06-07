class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # [1,2,1,0,4,2,6], k = 3
        q = deque([])
        res = []
        for i, num in enumerate(nums):
            if q and q[0] <= i - k:
                q.popleft()
            while q and nums[q[-1]] <= num:
                q.pop()
            q.append(i)
            if i >= k - 1:
                res.append(nums[q[0]])

        return res


        1,3,1,2,0,5