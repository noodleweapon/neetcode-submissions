class Solution:
    def decodeString(self, s: str) -> str:
        C = [1]
        S = ['']

        for c in s:
            if c == '[':
                rep = S[-1][-1]
                S[-1] = S[-1][:-1]
                C.append(int(rep))
                S.append("")
            elif c == ']':
                text = S.pop()
                reps = C.pop()
                S[-1] += text * reps
            else:
                S[-1] += c
        
        return S[0]


        # 2[a3[b]]c