class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        for i1 in reversed(range(len(num1))):
            for i2 in reversed(range(len(num2))):
                res += int(math.pow(10, i1 + i2)) * int(num1[i1]) * int(num2[i2])
        
        return str(res)