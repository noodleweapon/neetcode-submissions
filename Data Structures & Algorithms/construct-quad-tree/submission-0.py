"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def helper(r, c, n):
            if n == 1:
                return Node(grid[r][c], True)
            
            m = n // 2
            topL = helper(r, c, m)
            topR = helper(r, c + m, m)
            botL = helper(r + m, c, m)
            botR = helper(r + m, c + m, m)
            if topL.isLeaf and topR.isLeaf and botL.isLeaf and botR.isLeaf:
                if len(set([topL.val, topR.val, botL.val, botR.val])) == 1:
                    return Node(topL.val, True)
            return Node(0, False, topL, topR, botL, botR)
        
        return helper(0, 0, len(grid))