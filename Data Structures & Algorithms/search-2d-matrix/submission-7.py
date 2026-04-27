class Solution:
    def getYX(self, i, Y, X):
        y = i // X
        x = i % X
        return [y, x]
    
    def recOld(self, matrix, target, lowi, highi):
        Y = len(matrix)
        X = len(matrix[0])
        mi = ((highi - lowi) // 2) + lowi
        miy, mix = self.getYX(mi, Y, X)
        miv = matrix[miy][mix]
        if lowi == highi:
            return miv == target

        if miv == target:
            return True
        if target > miv:
            return self.rec(matrix, target, mi+1, highi)
        else:
            return self.rec(matrix, target, lowi, mi - 1)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Y = len(matrix)
        X = len(matrix[0])

        li = 0
        ri = X * Y - 1
        while li <= ri:
            mi = ((ri - li) // 2) + li
            my, mx = self.getYX(mi, Y, X)
            mv = matrix[my][mx]
            if li == ri:
                return mv == target
            if mv == target:
                return True
            if target > mv:
                li = mi + 1
            else:
                ri = mi - 1
        return False
        
        # return self.rec(matrix, target, 0, len(matrix) - 1)
