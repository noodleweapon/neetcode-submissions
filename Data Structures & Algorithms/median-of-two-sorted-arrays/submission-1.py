class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2
        is_even = total % 2 == 0

        A = [float("-inf")] + A + [float("inf")]
        B = [float("-inf")] + B + [float("inf")]

        l = 0
        r = len(A) - 1
        while l <= r:
            m1 = (l + r) // 2
            m2 = half - m1
            print(m1, m2)

            if A[m1 + 1] < B[m2]:
                l = m1 + 1
            elif A[m1] > B[m2 + 1]:
                r = m1 - 1
            else:
                if is_even:
                    left_partition_max = max(A[m1], B[m2])
                    right_partition_min = min(A[m1 + 1], B[m2 + 1])
                    return (left_partition_max + right_partition_min) / 2
                else:
                    return min(A[m1 + 1], B[m2 + 1])
