class Solution:
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        n = len(nums)
        def findFirst():
            l, r = 0, n - 1
            while l < r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            # l is first such that nums[l] >= target
            return l if nums[l] == target else -1
        
        def findLast():
            l, r = 0, n - 1
            while l < r:
                m = (l + r + 1) // 2
                if nums[m] > target:
                    r = m - 1 
                else:
                    l = m
            # l is first such that nums[l] <= target
            return l if nums[l] == target else -1
        
        return [findFirst(), findLast()]