class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            L, M, R = nums[l], nums[m], nums[r]
            if target == M:
                return m
            if L < M: # left is sorted
                if target < L:
                    l = m + 1
                elif target > M:
                    l = m + 1
                else:
                    r = m - 1
            elif L > M: # right is sorted
                if target < M:
                    r = m - 1
                elif target > R:
                    r = m - 1
                else:
                    l = m + 1
            else: # L == M
                l += 1

        return -1

        8,9,1,2,3,4,5,6,7

        3,4,5,6,1,2
        1,2,3,4,5,6