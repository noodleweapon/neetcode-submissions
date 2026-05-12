class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for i in range(len(nums)):
            newPerms = []
            for perm in perms:
                for j in range(len(perm) + 1):
                    newPerm = perm.copy()
                    newPerm.insert(j, nums[i])
                    newPerms.append(newPerm)
            perms = newPerms
        return perms


    def rec(self, i, nums):
        if i == len(nums):
            return [[]]
        
        perms = self.rec(i + 1, nums)
        newPerms = []
        for perm in perms:
            for j in range(0, len(perm) + 1):
                newPerm = perm.copy()
                newPerm.insert(j, nums[i])
                newPerms.append(newPerm)
        
        return newPerms

    def permuteRec(self, nums: List[int]) -> List[List[int]]:
        return self.rec(0, nums)