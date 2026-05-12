class Solution:
    def decodeString(self, s: str) -> str:
        C = [1]
        S = ['']
        num_str = ""

        for c in s:
            if c == '[':
                S.append("")
                C.append(int(num_str))
                num_str = ""
            elif c == ']':
                text = S.pop()
                reps = C.pop()
                S[-1] += text * reps
            else:
                if c in "0123456789":
                    num_str += c
                else:
                    S[-1] += c
        
        return S[0]
