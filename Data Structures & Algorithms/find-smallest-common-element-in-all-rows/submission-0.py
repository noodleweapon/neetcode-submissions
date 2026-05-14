class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        R = len(mat)
        C = len(mat[0])
        h = []
        d = defaultdict(int)
        for r in range(R):
            heapq.heappush(h, (mat[r][0], 0, r))
            d[mat[r][0]] += 1
        
        while h:
            val, c, r = heapq.heappop(h)
            if d[val] == R:
                return val
            if c >= C - 1:
                continue
            heapq.heappush(h, (mat[r][c + 1], c + 1, r))
            d[mat[r][c + 1]] += 1
        
        return -1

        # [1,2,3,4,5]
        # [7,9,11,12,14]

        # [5]
        # [5,8,10]
        # [5,7,9,11]
        # [5,7,9]

        # [1,2,3,4,5]
        # [2,4,5,8,10]
        # [3,5,7,9,11]
        # [1,3,5,7,9]
        # Naive approach: Use a counter, iterate keys, find min elem w R freq.

        # Heap pointer approach:
        # pop R items.

        # arr = nsmallest(R, h)
        # if len(arr) < R:
        #     return -1
        
        
