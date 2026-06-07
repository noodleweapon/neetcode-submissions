class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = Counter(t)
        missing = sum(d.values())
        print(missing)
        res = ""
        M = float("inf")
        l = 0
        for r in range(len(s)):
            if d[s[r]] > 0:
                missing -= 1
            d[s[r]] -= 1
            while l < len(s) and d[s[l]] < 0:
                d[s[l]] += 1
                l += 1
            if missing == 0:
                m = r - l + 1
                if m < M:
                    M = m
                    res = s[l:r + 1]

        return res

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         d = Counter(t)
#         res = ""
#         M = float("inf")
#         l = 0
#         S = set(list(t))
#         for r in range(len(s)):
#             d[s[r]] -= 1
#             while l < len(s) and d[s[l]] < 0:
#                 d[s[l]] += 1
#                 l += 1

#             if d[s[r]] <= 0:
#                 is_valid = True
#                 for char in S:
#                     if d[char] > 0:
#                         is_valid = False
#                         break
#                 if is_valid:
#                     m = r - l + 1
#                     if m < M:
#                         M = m
#                         res = s[l:r + 1]

#         return res

        # OUZODYXAZV
        # XYZ


        # OUZODYXAZZZV
        # XYZZZ