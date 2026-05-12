class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def rec(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return
            next_i = i + 1
            while next_i < len(nums) and nums[next_i] == nums[i]:
                next_i += 1
            
            for _ in range(next_i - i + 1):
                rec(next_i, subset)
                subset.append(nums[i])
            for _ in range(next_i - i + 1):
                subset.pop()

        rec(0, [])
        return res
        
        # rec(0, [])



        # 1,1,1,2

        # _,_,_,2 or _
        # 1,_,_,2 or _
        # 1,1,_,2 or _
        # 1,1,1,2 or _