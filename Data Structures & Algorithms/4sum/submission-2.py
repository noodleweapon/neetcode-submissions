class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        if n < 4:
            return []
        
        res = set()
        for l in range(1, n - 2):
            for r in range(l + 1, n - 1):
                L = l - 1
                R = r + 1
                while L >= 0 and R < n:
                    s = (nums[L], nums[l], nums[r], nums[R])
                    S = sum(s)
                    if S < target:
                        R += 1
                    elif S > target:
                        L -= 1
                    else:
                        res.add(s)
                        R += 1
                        L -= 1

        return list(res)

        # [-3, -2, 0, 2, 3]



