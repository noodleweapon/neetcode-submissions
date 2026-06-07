class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for token in tokens:
            if token == "+":
                right, left = s.pop(), s.pop()
                s.append(right + left)
            elif token == "*":
                right, left = s.pop(), s.pop()
                s.append(right * left)
            elif token == "-":
                right, left = s.pop(), s.pop()
                s.append(left - right)
            elif token == "/":
                right, left = s.pop(), s.pop()
                s.append(int(left / right))
            else:
                s.append(int(token))
        return s[0]