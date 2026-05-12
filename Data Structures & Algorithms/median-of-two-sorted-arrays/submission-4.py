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

            if al <= br and bl <= ar:
                if total % 2 == 1: # odd
                    return min(ar, br)
                return (max(al, bl) + min(ar, br)) / 2

            if al > br:
                r = i - 1
            elif bl > ar:
                l = i + 1