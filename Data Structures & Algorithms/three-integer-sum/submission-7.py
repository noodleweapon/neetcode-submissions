class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        hashes = set()
        out = []
        
        for k in range(1, len(nums) - 1):

            i = k - 1
            j = k + 1
            while i >= 0 and j < len(nums):
                S = nums[i] + nums[j] + nums[k]
                if S == 0:
                    hashed = str(nums[i]) + ',' + str(nums[k]) + ',' + str(nums[j])
                    if hashed not in hashes:
                        hashes.add(hashed)
                        out.append([nums[i], nums[k], nums[j]])
                    i -= 1
                    j += 1
                elif S > 0:
                    i -= 1
                else:
                    j += 1
        
        return list(map(list, out))