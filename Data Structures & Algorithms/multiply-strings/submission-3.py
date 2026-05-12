# could be faster!!
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                d1 = int(num1[-1 - i1])
                d2 = int(num2[-1 - i2])
                res += (10 ** (i1 + i2)) * d1 * d2
        
        return str(res)