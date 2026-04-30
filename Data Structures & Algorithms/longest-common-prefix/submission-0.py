class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        for i, c in enumerate(strs[0]):
            for s in strs[1:]:
                if s[i] != c:
                    return s[:i]
        return strs[0]