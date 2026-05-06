class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def get_sft(): # index of min
            if n == 1 or nums[0] < nums[-1]:
                return 0
            l, r = 0, n - 2
            while l <= r:
                m = (l + r) // 2
                L, M, R = nums[l], nums[m], nums[r]
                if M < R:
                    r = m - 1
                else:
                    l = m + 1
            return r
        
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