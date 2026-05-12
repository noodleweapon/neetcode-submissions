class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort(reverse=True)
        N = len(nums)

        out = []
        def rec(i, rem, items):
            if rem < 0:
                return
            if i == N:
                if rem == 0:
                    out.append(items.copy())
                return

            items.append(nums[i])
            rec(i, rem - nums[i], items)
            items.pop()
            rec(i + 1, rem, items)
        
        rec(0, target, [])
        return out