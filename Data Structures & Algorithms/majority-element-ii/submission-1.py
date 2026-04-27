class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        k = len(nums) // 3
        majs = []
        for num in nums:
            d[num] += 1
            if d[num] == k + 1:
                majs.append(num)
        return majs