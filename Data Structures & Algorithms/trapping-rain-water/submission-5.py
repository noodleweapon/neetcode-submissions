class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        water = 0
        leftMax, rightMax = height[l], height[r]
        while l < r:
            if leftMax < rightMax:
                water += leftMax - height[l]
                l += 1
                leftMax = max(leftMax, height[l])
            else:
                water += rightMax - height[r]
                r -= 1
                rightMax = max(rightMax, height[r])
                        
        return water

        # [4,2,0,3,2,5]