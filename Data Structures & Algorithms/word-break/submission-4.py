class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        memo = {}
        def rec(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]

            for word in words:
                if not s[i:].startswith(word):
                    continue
                
                if rec(i + len(word)):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        
        return rec(0)