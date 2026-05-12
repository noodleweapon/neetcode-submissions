class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        if n < 4:
            return []
        
        res = []
        for l in range(0, n - 3):
            if l > 0 and nums[l] == nums[l - 1]:
                continue
            for r in range(l + 1, n - 2):
                if r > l + 1 and nums[r] == nums[r - 1]:
                    continue
                L = r + 1
                R = n - 1
                while L < R:
                    s = [nums[L], nums[l], nums[r], nums[R]]
                    S = sum(s)
                    if S < target:
                        L += 1
                    elif S > target:
                        R -= 1
                    else:
                        res.append(s)
                        L += 1
                        R -= 1
                        while L < R and nums[L] == nums[L - 1]:
                            L += 1
                        while L < R and nums[R] == nums[R + 1]:
                            R -= 1

        return list(res)

        # [-3, -2, 0, 2, 3]



