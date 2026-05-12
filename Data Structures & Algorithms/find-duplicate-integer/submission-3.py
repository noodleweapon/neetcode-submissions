class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast_ind = 0
        slow_ind = 0
        while True:
            slow_ind = nums[slow_ind]
            fast_ind = nums[nums[fast_ind]]
            if slow_ind == fast_ind:
                break

        tail_ind = 0
        while slow_ind != tail_ind:
            tail_ind = nums[tail_ind]
            slow_ind = nums[slow_ind]
        return tail_ind