class Solution:
    def findInMountainArray(self, target: int, nums: 'MountainArray') -> int:
        def find_peak_ind():
            l, r = 0, nums.length() - 2
            while l <= r: # invariant: Peak is between l and r.
                m = (l + r) // 2
                L, M, R = nums.get(m - 1), nums.get(m), nums.get(m + 1)
                if M < R:
                    l = m + 1
                elif L > M:
                    r = m - 1
                else:
                    return m
        
        def find_in_left(l, r):
            while l <= r:
                m = (l + r) // 2
                v = nums.get(m)
                if v > target:
                    r = m - 1
                elif v < target:
                    l = m + 1
                else:
                    return m
            return -1

        def find_in_right(l, r):
            while l <= r:
                m = (l + r) // 2
                v = nums.get(m)
                if v < target:
                    r = m - 1
                elif v > target:
                    l = m + 1
                else:
                    return m
            return -1

        peak = find_peak_ind()
        if nums.get(peak) == target:
            return peak
        left = find_in_left(0, peak - 1)
        if left != -1:
            return left
        return find_in_right(peak + 1, nums.length() - 1)



        # 1,2,3,4,2,1
        # target = 6
        # -5,-4,-3,2,4,5


        # 1,2,  3,4,2,1
        # -5,-4,3,2,4,5

        # 1,2,3,4,2,1