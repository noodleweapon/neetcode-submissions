class Solution:
    def isValid(self, text: str) -> bool:
        s = []
        for c in text:
            if c in ['(', '[', '{']:
                s.append(c)
                continue
            if not s:
                return False
            top = s.pop()
            if c == ')' and top != '(':
                return False
            if c == ']' and top != '[':
                return False
            if c == '}' and top != '{':
                return False
        return len(s) == 0