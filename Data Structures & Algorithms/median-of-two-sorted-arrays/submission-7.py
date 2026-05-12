class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        A = [float("-inf")] + A + [float("inf")]
        B = [float("-inf")] + B + [float("inf")]

        total = len(nums1) + len(nums2)
        half = total // 2

        l, r = 0, len(A) - 2

        while True:
            i = (l + r) // 2
            j = half - i
            al, ar = A[i], A[i + 1]
            bl, br = B[j], B[j + 1]

            if ar < bl:
                l = i + 1
            elif br < al:
                r = i - 1
            else:
                if half * 2 == total: # even
                    return (max(al, bl) + min(ar, br)) / 2
                else:
                    return min(ar, br)

