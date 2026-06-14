class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        def get_steps(val):
            s = 0
            while val >= 5:
                val -= 3
                s += 1
            if val == 4:
                return 2 + s
            else:
                return 1 + s

        steps = 0
        for key, val in counter.items():
            if val == 1:
                return -1
            steps += get_steps(val)
        return steps