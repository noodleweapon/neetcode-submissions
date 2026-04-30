class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0

        mid = len(nums) // 2
        if nums[mid] == target:
            return mid
        if target < nums[mid]:
            li = self.search(nums[0:mid], target)
            if li != -1:
                return li
        else:
            ri = self.search(nums[mid+1:], target)
            if ri != -1:
                return ri + mid + 1
        return -1
