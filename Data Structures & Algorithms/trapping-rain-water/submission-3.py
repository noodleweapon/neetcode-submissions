class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        water = 0
        level = min(height[l], height[r])
        while l < r:
            if height[l] < height[r]:
                water += max(0, level - height[l])
                l += 1
            else:
                water += max(0, level - height[r])
                r -= 1
            
            level = max(level, min(height[l], height[r]))
            
        return water

        [4,2,0,3,2,5]