class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        n = len(nums)
        for j in range(1, n - 1):
            i = j - 1
            k = j + 1
            while i >= 0 and k < n:
                def exceeds():
                    return nums[i] + nums[j] + nums[k] >= target
                while i > 0 and exceeds():
                    i -= 1
                if exceeds():
                    break
                res += i + 1
                k += 1
        
        return res
        
        # [-2-1,0,1,3]
        # target 1
