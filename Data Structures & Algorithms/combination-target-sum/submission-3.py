class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []
        def rec(i, items, rem):
            nonlocal nums, out
            if i == len(nums):
                if rem == 0:
                    out.append(list(items))
                return

            num = nums[i]
            N = rem // num

            rec(i + 1, items, rem)
            for j in range(N):
                items.append(num)
                new_rem = rem - num * (j + 1)
                rec(i + 1, items, new_rem)

            for j in range(N):
                items.pop()
        
        rec(0, [], target)
        return out