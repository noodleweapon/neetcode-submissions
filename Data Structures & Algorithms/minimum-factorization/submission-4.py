class Solution:
    def smallestFactorization(self, num: int) -> int:
        if num == 1:
            return 1
        res = 0
        count = 0
        for factor in [9,8,7,6,5,4,3,2]:
            while num % factor == 0:
                num /= factor
                res += (10 ** count) * factor
                count += 1
                if res >= (1 << 32):
                    return 0
        if num != 1:
            return 0
        return res

        # 2226 --> 48
        # 68
        # Input: num = 48
        # 48 --> factorize into one digit nums, and then sort 2...
        # 6 *8 = 48
        # 15
        # 3*5

