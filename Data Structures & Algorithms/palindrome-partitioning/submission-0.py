class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(t):
            for i in range(len(t) // 2):
                j = len(t) - 1 - i
                if t[i] != t[j]:
                    return False
            return True

        out = []
        def rec(i, items):
            if i == len(s):
                out.append(items.copy())
                return
            
            for j in range(i + 1, len(s) + 1):
                span = s[i:j]
                if not is_palindrome(span):
                    continue
                items.append(span)
                rec(j, items)
                items.pop()
        
        rec(0, [])
        return out