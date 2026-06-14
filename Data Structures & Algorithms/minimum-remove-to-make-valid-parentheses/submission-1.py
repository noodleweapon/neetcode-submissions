class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if s == '':
            return ''

        opens = 0
        res = []
        for c in s:
            if c == '(':
                opens += 1
                res.append('(')
            elif c == ')':
                if opens > 0:
                    opens -= 1
                    res.append(')')
            else:
                res.append(c)
        
        for i in reversed(range(len(res))):
            if opens == 0:
                break
            if res[i] == '(':
                res[i] = ''
                opens -= 1

        return ''.join(res)

        # ))()(( < -- fail
        # nee(t(c)o)de) OK
        # x(y)z( <-- fail
        