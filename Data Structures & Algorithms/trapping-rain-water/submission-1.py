class Solution:
    def trap(self, hs: List[int]) -> int:
        i = 0
        j = len(hs) - 1
        level = min(hs[i], hs[j])
        water = 0
        while i < j:
            L = hs[i]
            R = hs[j]
            
            if L < R:
                water += max(0, level - hs[i])
                i += 1
            else:
                water += max(0, level - hs[j])
                j -= 1
            
            new_level = min([L, R])
            level = max(level, new_level)
            
        return water
