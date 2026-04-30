class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for token in tokens:
            if token == "+":
                b, a = s.pop(), s.pop()
                s.append(a + b)
            elif token == "-":
                b, a = s.pop(), s.pop()
                s.append(b - a)
            elif token == "*":
                b, a = s.pop(), s.pop()
                s.append(a * b)
            elif token == "/":
                b, a = s.pop(), s.pop()
                s.append(a // b)
            else:
                s.append(int(token))
        return s.pop()