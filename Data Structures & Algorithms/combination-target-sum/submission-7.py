class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def rec(i, arr, s):
            if s > target:
                return
            if i == len(nums):
                if s == target:
                    res.append(arr.copy())
                return
            
            rec(i + 1, arr, s)
            arr.append(nums[i])
            rec(i, arr, s + nums[i])
            arr.pop()
        
        rec(0, [], 0)
        return res