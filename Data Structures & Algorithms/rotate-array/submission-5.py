class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def rev(l, r):
            nonlocal nums
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        n = len(nums)
        k %= n

        rev(0, n - 1)
        rev(0, k - 1)
        rev(k, n - 1)
        
        # [1,2,3,4,5,6,7,8], k = 3
        # [6,7,8,1,2,3,4,5]
