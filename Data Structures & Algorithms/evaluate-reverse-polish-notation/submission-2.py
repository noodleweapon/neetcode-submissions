class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for token in tokens:
            if token == "+":
                a = s.pop()
                b = s.pop()
                s.append(a + b)
            elif token == "-":
                a = s.pop()
                b = s.pop()
                s.append(a - b)
            elif token == "*":
                a = s.pop()
                b = s.pop()
                s.append(a * b)
            elif token == "/":
                a = s.pop()
                b = s.pop()
                s.append(a // b)
            else:
                s.append(int(token))
        return s.pop()