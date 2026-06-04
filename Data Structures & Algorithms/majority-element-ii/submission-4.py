class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        maj = n // 3
        c = Counter(nums)
        res = []
        for key in c:
            if c[key] > maj:
                res.append(key)
        return res