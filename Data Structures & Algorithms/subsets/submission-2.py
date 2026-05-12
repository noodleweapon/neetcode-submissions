class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = []
        def rec(i, items):
            nonlocal arr
            if i >= len(nums):
                arr.append(list(items)) # important it's here
                return
            items.append(nums[i])
            rec(i + 1, items)
            items.pop()
            rec(i + 1, items)
        
        rec(0, [])
        return arr
