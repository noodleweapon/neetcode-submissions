class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        q = deque([])
        i = 0
        while i < len(s):
            v = s[i]
            while v in q:
                q.popleft()
            
            q.append(v)
            i += 1
            if len(q) > m:
                m = len(q)
        return m