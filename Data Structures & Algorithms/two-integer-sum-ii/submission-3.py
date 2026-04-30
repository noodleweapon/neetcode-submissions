class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(1, len(numbers)):
            a, b = numbers[i - 1], numbers[i]
            if (a + b) == target:
                return [i, i+1]
