class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        half = math.ceil((len(nums1) + len(nums2)) / 2)

        l = 0
        r = len(nums1) - 1
        while l <= r:
            m1 = (l + r) // 2
            m2 = half - m1 - 2
            print(m1, m2)
            return