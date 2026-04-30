class Solution:
    def getYX(self, i, Y, X):
        y = i // X
        x = i % X
        return [y, x]
    
    def rec(self, matrix, target, lowi, highi):
        Y = len(matrix)
        X = len(matrix[0])
        mi = ((highi - lowi) // 2) + lowi
        miy, mix = self.getYX(mi, Y, X)
        miv = matrix[miy][mix]
        if lowi == highi:
            return miv == target

        if miv == target:
            return True
        if miv > target:
            return self.rec(matrix, target, mi+1, highi)
        else:
            return self.rec(matrix, target, lowi, mi - 1)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.rec(matrix, target, 0, len(matrix) - 1)
