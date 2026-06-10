class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        elems = list(range(1, n + 1))
        res = []

        def rec(i, arr):
            if len(arr) == k:
                res.append(arr.copy())
                return
            if i == n:
                return
            
            rec(i + 1, arr)
            elems_missing = k - len(arr)
            opportunities = n - i
            if elems_missing > opportunities:
                return
            arr.append(elems[i])
            rec(i + 1, arr)
            arr.pop()

        rec(0, [])
        return res


        # n = 1,2,3,4,5
        # k = 3