class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = []
        for i, num in enumerate(nums):
            s.append((i, num))
        s.sort(key=lambda x: x[1])

        i = 0
        j = len(s) - 1
        while i < j:
            _sum = s[i][1] + s[j][1]
            if _sum > target:
                j -= 1
            elif _sum == target:
                break
            else:
                i += 1
        return [s[j][0], s[i][0]]