class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in reversed(range(len(digits))):
            n = carry + digits[i]
            digits[i] = n % 10
            carry = 1 if n >= 10 else 0

        if carry > 0:
            digits.insert(0, carry)
        
        return digits