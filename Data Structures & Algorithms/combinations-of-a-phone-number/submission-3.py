class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        m = [None, None, list('abc'), list('def'), list('ghi'), list('jkl'), list('mno'), list('pqrs'), list('tuv'), list('wxyz')]
        out = []
        def backtrack(i, items):
            if i == len(digits):
                out.append("".join(items))
                return
            options = m[int(digits[i])]
            for option in options:
                items.append(option)
                backtrack(i + 1, items)
                items.pop()
        
        backtrack(0, [])
        return out