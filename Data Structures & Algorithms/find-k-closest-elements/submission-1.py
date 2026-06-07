class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        h = []
        for z in arr:
            dist = abs(z - x)
            heapq.heappush(h, (dist, z))
        return list(sorted(map(lambda x: x[1], heapq.nsmallest(k, h))))

# Input: arr = [2,4,5,8], k = 2, x = 6

# h = [(1, 5), (2, 4), (2, 8), (4, 2)]

# Output: [4,5]

# Input: arr = [2,3,4], k = 3, x = 1

# Output: [2,3,4]
