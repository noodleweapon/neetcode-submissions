class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        perms = [[]]
        for i in range(len(nums)):
            newPerms = set()
            for perm in perms:
                for j in range(len(perm) + 1):
                    newPerm = perm.copy()
                    newPerm.insert(j, nums[i])
                    newPerms.add(newPerm)
            perms = list(newPerms)
        return perms
