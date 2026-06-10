class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total, n = sum(nums), len(nums)
        target = total // k
        if target * k != total:
            return False
        nums.sort(reverse=True)
        if nums[0] > target:
            return False
        
        seen = set()

        def rec(i, buckets):
            key = (i, *sorted(buckets))
            if key in seen:
                return False
            if i == n:
                return max(buckets) == min(buckets) == target

            for j in range(k):
                if buckets[j] + nums[i] > target:
                    continue
                buckets[j] += nums[i]
                if rec(i + 1, buckets):
                    return True
                buckets[j] -= nums[i]
            seen.add(key)
            return False
        
        return rec(0, [0] * k)
