class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = sorted(nums)
        i = 0
        j = len(s) - 1
        while i < j:
            _sum = s[i] + s[j]
            if _sum > target:
                j -= 1
            elif _sum == target:
                break
            else:
                i += 1
        return [nums.index(s[i]), nums.index(s[j])]