class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(A, B):
            res = []
            while A and B:
                if A[0] < B[0]:
                    res.append(A[0])
                    A.pop(0)
                else:
                    res.append(B[0])
                    B.pop(0)
            if A:
                res = res + A
            if B:
                res = res + B
            return res

        def mergesort(arr):
            k = len(arr)
            if k < 2:
                return arr
            A = mergesort(arr[:k//2])
            B = mergesort(arr[k//2:])
            return merge(A, B)
        
        return mergesort(nums)
