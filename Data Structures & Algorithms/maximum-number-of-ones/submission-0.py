class Solution:
    def maximumNumberOfOnes(self, C: int, R: int, sideLength: int, maxOnes: int) -> int:
        # In a 3*3 matrix, no 2*2 sub-matrix can have more than 1 one.
        # the key assumption is that the optimal packing of the matrix is done by TILEs
        h = []
        for r in range(sideLength):
            for c in range(sideLength):
                rCount = R // sideLength
                if R % sideLength >= (r + 1):
                    rCount += 1
                cCount = C // sideLength
                if C % sideLength >= (c + 1):
                    cCount += 1
                count = rCount * cCount
                heapq.heappush(h, count)
        
        return sum(heapq.nlargest(maxOnes, h))




        
        
        
        # occupied = [[False] * C for _ in range(R)]
        # convolutions = [[0] * (C - sideLength + 1) for _ in range(R - sideLength + 1)]
        # res = 0
        # def rec(i):
        #     nonlocal res
        #     if i > res:
        #         res = i
            
        #     for r in range(R):
        #         for c in range(C):
        #             if not occupied[r][c]:
        #                 occupied[r][c] = True
        #                 for x in range(-sideLength + 1, sideLength):

        #                 rec(i + 1)
        #                 occupied[r][c] = False
        
        # rec(0)

        
        # [1,0,1,0]
        # [0,0,0,0]
        # [1,0,1,0]
        # sidelength = 2

        # [2,2,0]
        # [2,2,0]
        # sidelength = 3
        # []

        # []

        