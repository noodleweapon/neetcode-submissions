class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        def rec(i):
            if i == len(s):
                return True
            for word in words:
                if not s[i:].startswith(word):
                    continue
                
                if rec(i + len(word)):
                    return True
            return False
        
        return rec(0)