class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        d = {}
        for i in range(n):
            number = numbers[i]
            if target - number in d:
                return [d[target - number] + 1, i + 1]
            d[number] = i
        