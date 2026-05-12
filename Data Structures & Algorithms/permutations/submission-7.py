class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        seen = [False] * len(nums)
        out = []
        def rec(i, perm):
            if i == len(nums):
                out.append(perm.copy())
                return
            
            for j in range(len(nums)):
                if seen[j]:
                    continue
                seen[j] = True
                perm.append(nums[j])
                rec(i + 1, perm)
                perm.pop()
                seen[j] = False
        
        rec(0, [])
        return out