class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m = [nums[0], nums[0]]
        p = [nums[0], nums[0]]
        for num in nums[1:]:
            if num == 0:
                p = [num, num]
                m[0] = min(m[0], p[0])
                m[1] = max(m[1], p[1])
            else:
                A = num * p[0]
                B = num * p[1]
                p[0] = min([num, A, B])
                p[1] = max([num, A, B])

                m[0] = min(m[0], p[0])
                m[1] = max(m[1], p[1])
        return m[1]

