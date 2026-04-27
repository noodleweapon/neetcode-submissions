from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
            if d[num] == 2:
                return True
        return False