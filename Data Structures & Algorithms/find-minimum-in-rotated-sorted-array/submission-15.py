class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1 # invariant: min element is in here.
        while l < r:
            m = (l + r) // 2

            if nums[l] < nums[m]:
                if nums[m] < nums[r]: # l < m < r
                    r = m - 1
                elif nums[m] > nums[r]: # l < m > r --> implies l > r
                    l = m + 1
            elif nums[l] > nums[m]:
                if nums[m] < nums[r]: # l > m < r
                    l = l + 1
                    r = m
                elif nums[m] > nums[r]: # l > m > r, impossible
                    print("impossible")
            elif l == m:
                if nums[m] < nums[r]:
                    r = m
                elif nums[m] > nums[r]:
                    l = m + 1
        return nums[l]



        # [3,4,5,6,1,2]
        #  2   3     1
        
        # [1,2,3,4,5,6]
        #  1   2     3
        

        # 123
        # 132
        # 1
        #  3   1.    2

