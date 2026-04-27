class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        
        def rec(s, rem_opens, rem_closes):
            if rem_opens == 0 and rem_closes == 0:
                out.append(s)
                return
            if rem_opens > 0:
                rec(s + "(", rem_opens - 1, rem_closes)
            if rem_closes > 0 and rem_closes > rem_opens:
                rec(s + ")", rem_opens, rem_closes - 1)

        rec("", n, n)
        return out