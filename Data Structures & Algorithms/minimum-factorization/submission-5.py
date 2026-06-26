class Solution:
    def smallestFactorization(self, num: int) -> int:
        if num == 1:
            return 1
        res = 0
        mul = 1
        for factor in [9,8,7,6,5,4,3,2]:
            while num % factor == 0:
                num //= factor
                res += mul * factor
                mul *= 10
                if res >= (1 << 32): # THIS LINE WAS TRICKY.
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

