class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        arr = [(i, v) for i, v in enumerate(numbers)]
        arr.sort(key=lambda x: x[1])
        i = 0
        j = len(numbers) - 1
        while i < j:
            diff = arr[i][1] + arr[j][1] - target
            if diff > 0:
                j -= 1
            elif diff < 0:
                i += 1
            else:
                break
        return [arr[i][0] + 1, arr[j][0] + 1]