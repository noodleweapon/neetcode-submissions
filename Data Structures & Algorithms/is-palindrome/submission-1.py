class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while True:
            while not s[l].isalnum():
                l += 1
            
            while not s[r].isalnum():
                r -= 1

            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
