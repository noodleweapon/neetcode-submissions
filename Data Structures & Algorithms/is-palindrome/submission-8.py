class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True
        l = 0
        r = len(s) - 1

        while True:
            while not s[l].isalnum():
                if not l < len(s) - 1:
                    break
                l += 1
            
            while not s[r].isalnum():
                if not r > 0:
                    break
                r -= 1

            if lower(s[l]) != lower(s[r]):
                return False
            
            if l < len(s) - 1:
                l += 1
            if r > 0:
                r -= 1
            if l >= r:
                break
        
        return True
