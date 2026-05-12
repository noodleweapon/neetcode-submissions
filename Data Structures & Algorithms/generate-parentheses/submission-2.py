class Solution:
    def rec(self, i, j, n, cur, res):
        if i == n and j == n:
            res.append("".join(cur))
        
        if i < n:
            cur.append("(")
            self.rec(i + 1, j, n, cur, res)
            cur.pop()
        if j < i:
            cur.append(")")
            self.rec(i, j + 1, n, cur, res)
            cur.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        cur, res = [], []
        self.rec(0, 0, n, cur, res)
        return res
        