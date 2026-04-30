class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if self.isOpen(char):
                stack.append(char)
            else:
                top = stack[-1]
                if not self.isValidMatch(top, char):
                    return False
                stack.pop()
        return True
    
    def isOpen(self, char):
        match char:
            case "[":
                return True
            case "{":
                return True
            case "(":
                return True
            case _:
                return False

    def isValidMatch(self, opening, closing):
        pairs = {'(': ')', '{': '}', '[': ']'}
        return pairs.get(opening) == closing
