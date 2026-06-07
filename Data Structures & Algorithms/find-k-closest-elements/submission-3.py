class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k

        while l < r:
            m = (l + r) // 2
            cond = x - arr[m] <= arr[m + k] - x
            if not cond:
                l = m + 1
            else:
                r = m
        return arr[l:l + k]


        # [2,4,5,8], k = 2, x = 6