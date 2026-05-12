from collections import deque
import heapq

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        res = 0
        for c in charSet:
            count = 0
            l = 0
            for r, char in enumerate(s):
                if char == c:
                    res = max(res, r - l + 1)
                    continue
                count += 1
                while count > k:
                    if s[l] != c:
                        count -= 1
                    l += 1
                else:
                    res = max(res, r - l + 1)
        return res

                
                
                