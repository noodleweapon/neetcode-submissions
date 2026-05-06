class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)

        def find_shift():
            l, r = 0, n - 1
            while l < r:
                m = (l + r) // 2 # leftmost true.
                if nums[m] < nums[r]:
                    r = m
                else:
                    l = m + 1
            return l

        
        def includes():
            shf = find_shift() # index of smallest(min)
            print(shf)
            l, r = 0, n - 1
            while l <= r:
                m = (l + r) // 2
                M = (m + shf) % n
                if target < nums[M]:
                    r = m - 1
                elif target > nums[M]:
                    l = m + 1
                else:
                    return True

            return False

        return includes()