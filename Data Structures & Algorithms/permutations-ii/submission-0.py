class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for i in range(len(nums)):
            newPerms = []
            for perm in perms:
                for j in range(len(perm) + 1):
                    newPerm = perm.copy()
                    newPerm.insert(j, nums[i])
                    if newPerms and newPerms[-1] == newPerm:
                        continue
                    newPerms.append(newPerm)
            perms = newPerms
        return perms
