class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()
        for i in range(1, n - 1):
            l = i - 1
            r = i + 1
            while l >= 0 and r < n:
                s = nums[l] + nums[i] + nums[r]
                if s < 0:
                    r += 1
                elif s > 0:
                    l -= 1
                else:
                    res.add((nums[l], nums[i], nums[r]))
                    r += 1
                    l -= 1

        return list(res)

        # [-4,-1,-1,0,1,2]



        
        # [0,0,0,0,0]
        # [-2,-1,0,1,2]
        



