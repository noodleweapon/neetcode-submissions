class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        S = sum(nums) #
        if S % k != 0: #
            return False #
        target = S // k #
        visited = set() #
        
        def dfs(i, buckets): #
            if i == len(nums): #
                for j in range(k):
                    if buckets[j] != target:
                        return False
                return True

            for j in range(k):
                buckets[j] += nums[i]
                key = (i + 1, *sorted(buckets))
                if buckets[j] <= target and key not in visited:
                    visited.add(key)
                    if dfs(i + 1, buckets):
                        return True
                buckets[j] -= nums[i]
            
            return False
        init = [0] * k
        visited.add((0, *init))
        return dfs(0, init)

        # [2,4,1,3,5]
        # [2,0,0,0,0]
        # [0,2,0,0,0]



        # [5], [2,3], [4,1]