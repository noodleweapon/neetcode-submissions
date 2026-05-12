class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def get_sft(): # index of min
            l, r = 0, n - 1
            # invariant: min is inside [l, r]
            while l < r:
                m = (l + r) // 2
                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m
            return l

        def get_ind(sft):
            l, r = 0, n - 1
            while l <= r:
                m = (l + r) // 2
                M = nums[(m + sft) % n]
                if M < target:
                    l = m + 1
                elif target < M:
                    r = m - 1
                else:
                    return (m + sft) % n
            return -1
        
        sft = get_sft()
        return get_ind(sft)