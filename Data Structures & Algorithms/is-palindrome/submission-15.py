class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = list(filter(lambda x: x.isalnum() and s != ' ', list(s.lower())))
        return ''.join(a) == ''.join(list(reversed(a)))