class Solution:
    def isValid(self, s: str) -> bool:
        s = []
        for c in s:
            if c in ['(', '[', '{']:
                s.append(c)
                continue
            top = s.pop()
            if c == ')' and top != '(':
                return False
            if c == ']' and top != '[':
                return False
            if c == '}' and top != '{':
                return False
        return len(s) == 0