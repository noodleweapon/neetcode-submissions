class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        seq = []
        i = 0
        while i < len(s):
            v = s[i]
            while v in seq:
                seq.pop(0)
            
            seq.append(v)
            i += 1
            if len(seq) > m:
                m = len(seq)
        return m