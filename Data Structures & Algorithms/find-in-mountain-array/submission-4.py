class Solution:
    def findInMountainArray(self, target: int, nums: 'MountainArray') -> int:
        def find_peak_ind():
            l, r = 1, nums.length() - 2
            while l < r: # invariant: Peak is between l and r.
                m = (l + r + 1) // 2
                cond = nums.get(m - 1) < nums.get(m)
                if cond:
                    l = m
                else:
                    r = m - 1
            return l
        
        def find(l, r, asc):
            while l <= r:
                m = (l + r) // 2
                v = nums.get(m)
                if v > target:
                    if asc:
                        r = m - 1
                    else:
                        l = m + 1

                elif v < target:
                    if asc:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    return m
            return -1

        peak = find_peak_ind()
        if nums.get(peak) == target:
            return peak
        left = find(0, peak - 1, True)
        if left != -1:
            return left
        return find(peak + 1, nums.length() - 1, False)



        # 1,2,3,4,2,1
        # target = 6
        # -5,-4,-3,2,4,5


        # 1,2,  3,4,2,1
        # -5,-4,3,2,4,5

        # 1,2,3,4,2,1