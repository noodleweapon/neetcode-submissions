class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        res = nums[0]
        while i <= j:
            if nums[i] < nums[j]:
                res = min(res, nums[i])
                break
                
            k = (i + j) // 2
            res = min(res, nums[k])

            left_sorted = nums[i] < nums[k]
            if left_sorted:
                i = k + 1
            else:
                j = k - 1
            
        return res




    # def findMin(self, nums: List[int]) -> int:
    #     if len(nums) == 1:
    #         return nums[0]
    #     if nums[0] < nums[-1]:
    #         return nums[0]
    #     i = 1
    #     j = len(nums) - 1
    #     while i <= j:
    #         k = (i + j) // 2
    #         if nums[k - 1] > nums[k]:
    #             return nums[k]

    #         if nums[k] < nums[j]:
    #             j = k
    #         elif nums[i] < nums[k - 1]:
    #             i = k
    #         else:
    #             i += 1

    #     return -1
