class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        j = 0
        prv = 0
        res = 1
        for i in range(1, n):
            cur = max(min(arr[i] - arr[i - 1], 1), -1)
            if cur == 0:
                j = i
            elif cur == prv:
                j = i - 1
            prv = cur
            res = max(res, i - j + 1)
        
        return res


# class Solution:
#     def maxTurbulenceSize(self, arr: List[int]) -> int:
#         n = len(arr)
#         res = 1
#         directions = []
#         for i in range(1, n):
#             if arr[i] == arr[i - 1]:
#                 M = 1
#                 directions = []
#                 continue
#             direction = 1 if arr[i] > arr[i - 1] else -1

#             if directions and directions[-1] == direction:
#                 directions = [direction]
#             else:
#                 directions.append(direction)
#             res = max(res, len(directions) + 1)
        
#         return res
