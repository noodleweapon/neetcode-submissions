class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1 # inv: Min elem is here.
        while l < r:
            m = (l + r) // 2
            cond = nums[m] > nums[r]
            if cond:
                l = m + 1
            else:
                r = m # naturally floors.
        o = l
        print(o)
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            M = nums[(m + o) % n]
            if M < target:
                l = m + 1
            elif M > target:
                r = m - 1
            else:
                return (m + o) % n
        
        return -1
                
        # # l, r = 0, n - 1


        
        # [3,4,<5,6,1,2>]
        # [1,2,3,4,5,6]