class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        n = len(nums)
        for j in range(1, n - 1):
            i = j - 1
            k = j + 1
            while i >= 0 and k < n:
                while i > 0 and nums[i] + nums[j] + nums[k] >= target:
                    i -= 1
                if nums[i] + nums[j] + nums[k] >= target:
                    break
                res += i + 1
                k += 1
        
        return res
        
        # [-2-1,0,1,3]
        # target 1
