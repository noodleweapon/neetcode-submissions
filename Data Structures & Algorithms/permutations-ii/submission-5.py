class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        def rec(i, arr, used):
            if i == len(nums):
                res.append(arr.copy())
                return
            for j in range(n):
                if used[j]:
                    continue
                if j > 0 and nums[j] == nums[j - 1] and (not used[j - 1]):
                    continue
                used[j] = True
                arr.append(nums[j])

                rec(i + 1, arr, used)

                used[j] = False
                arr.pop()

        rec(0, [], [False] * n)
        return res


        # [1,1,2]
        # [1,]