class Solution:
    def decodeString(self, s: str) -> str:
        stack = ['']
        num_str = ''
        for i in range(len(s)):
            c = s[i]
            if c in list('0123456789'):
                num_str += c
            elif c == '[':
                stack.append(int(num_str))
                stack.append('')
                num_str = ''
            elif c == ']':
                text, reps = stack.pop(), stack.pop()
                stack[-1] += text * reps
            else:
                stack[-1] += c
        
        return stack[0]

        # axb3[z]4[c]
        # ab12[c]3[d]1[x]
        # 2[a3[b]]c
