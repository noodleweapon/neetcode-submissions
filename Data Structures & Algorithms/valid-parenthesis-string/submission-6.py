class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = 0
        hi = 0

        for c in s:
            if c == '*':
                lo -= 1
                hi += 1
            elif c == '(':
                lo += 1
                hi += 1
            elif c == ')':
                lo -= 1
                hi -= 1
            
            if lo < 0:
                lo = 0
            if hi < 0:
                return False

        return lo <= 0 and hi >= 0