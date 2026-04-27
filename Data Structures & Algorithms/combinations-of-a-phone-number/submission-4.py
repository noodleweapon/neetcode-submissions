class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        m = [None, None, list('abc'), list('def'), list('ghi'), list('jkl'), list('mno'), list('pqrs'), list('tuv'), list('wxyz')]
        out = []
        def backtrack(i, s):
            if i == len(digits):
                out.append(s)
                return
            for option in m[int(digits[i])]:
                backtrack(i + 1, s + option)
        
        backtrack(0, "")
        return out