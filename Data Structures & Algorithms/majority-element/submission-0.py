class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        n = len(nums) // 2
        for num, f in c.items():
            if f > n:
                return num