class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if n <= 2:
            return nums in target

        def find_shift():
            if nums[0] < nums[-1]:
                return 0
            l, r = 0, n - 2 # possible i where i+1 is start(min).
            while l <= r:
                m = (l + r) // 2
                if nums[m] > nums[m + 1]:
                    return m + 1
                if nums[m] < nums[r]:
                    r = m - 1
                if nums[l] < nums[m]:
                    l = m + 1
        
        shf = find_shift() # index of smallest(min)
        print(shf, nums[shf])
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            M = (m + shf) % n
            print(nums[M])
            if target < nums[M]:
                r = m - 1
            elif target > nums[M]:
                l = m + 1
            else:
                return True

        return False

        # [3,4,5,6,1,2,3]