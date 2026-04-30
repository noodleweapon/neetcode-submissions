import copy
class Solution:
    def rec(self, i, digits, cur, res):
        m = {
            "2": list("abc"),
            "3": list("def"),
            "4": list("ghi"),
            "5": list("jkl"),
            "6": list("mno"),
            "7": list("pqrs"),
            "8": list("tuv"),
            "9": list("wxjz"),
        }

        if len(cur) == len(digits):
            res.append("".join(cur))
            return
        if i >= len(digits):
            return
        digit = digits[i]
        for c in m[digit]:
            cur.append(c)
            self.rec(i + 1, digits, cur, res)
            cur.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        cur, res = [], []
        self.rec(0, digits, cur, res)
        return res
