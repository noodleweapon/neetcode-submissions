class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        n = len(nums)
        g = [[] for _ in range(n + 1)]
        for items in sequences:
            for i in range(len(items) - 1):
                a, b = items[i], items[i + 1]
                g[a].append(b)

        for i in range(n - 1):
            a, b = nums[i], nums[i + 1]
            if b not in g[a]:
                return False
        
        return True

        # 1,2,3,4
        # 2->1
        # [1,2],[1,3],[2,3]




