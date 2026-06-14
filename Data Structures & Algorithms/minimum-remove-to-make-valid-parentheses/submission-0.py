class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if s == '':
            return 0
        
        opens = 0
        res = ""
        for c in s:
            if c == '(':
                opens += 1
                res += '('
            elif c == ')':
                if opens > 0:
                    opens -= 1
                    res += ')'
            else:
                res += c
        
        for _ in range(opens):
            for i in reversed(range(len(res))):
                if res[i] == '(':
                    res = res[:i] + res[i + 1:]
                    break

        return res

        # ))()(( < -- fail
        # nee(t(c)o)de) OK
        # x(y)z( <-- fail
        