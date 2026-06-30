class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        n = len(strs)
        def should_rev(s):
            l, r = 0, len(s) - 1
            while l < r:
                L, R = ord(s[l]), ord(s[r])
                if L < R:
                    return True
                elif L > R:
                    return False
                l += 1
                r -= 1
            return False
        
        def rev_if_better(s):
            if should_rev(s):
                return s[::-1]
            else:
                return s
        res = ""
        strs = list(map(rev_if_better, strs))
        for i in range(len(strs)):
            other = "".join(strs[i + 1:] + strs[:i])
            for option in [strs[i], strs[i][::-1]]:
                for j in range(len(option)):
                    text = option[j:] + other + option[:j]
                    if text > res:
                        res = text
        return res



        # text = ""
        # for s in strs:
        #     if should_rev(s):
        #         text += str(reversed(s))
        #     else:
        #         text += s
        
        # caab --> cbaa
        # whereas caab --> bcaa. BAD

        # xyz, xyz
        # xyz, zyx
        # zzyxxy

        # "abc","xyz",

        
            
