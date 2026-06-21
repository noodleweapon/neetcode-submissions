class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def f(x):
            return (a * x * x) + (b * x) + c
        
        if a == 0:
            if b >= 0:
                return list(map(f, nums))
            else:
                return list(reversed(list(map(f, nums))))

        
        tip = -b / (2 * a) # 2ax + b = 0
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            cond = nums[m] >= tip
            if cond:
                r = m
            else:
                l = m + 1
        
        l, r = l - 1, l
        res = []
        while len(res) < n:
            if not (0 <= l < n):
                res.append(f(nums[r]))
                r += 1
                continue
            if not (0 <= r < n):
                res.append(f(nums[l]))
                l -= 1
                continue
            if (tip - nums[l]) <= (nums[r] - tip):
                res.append(f(nums[l]))
                l -= 1
            else:
                res.append(f(nums[r]))
                r += 1
        if a < 0:
            return list(reversed(res))
        return res
