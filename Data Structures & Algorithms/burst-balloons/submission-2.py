class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)

        def rec(l, r): # l is included, r is excluded
            v = 0
            for m in range(l, r):
                p = nums[l - 1] * nums[m] * nums[r]
                z = rec(l, m) + rec(m + 1, r) + p
                v = max(v, z)
            return v
        return rec(1, n - 1)


        # popped = [False] * n

        # def get_l(ind):
        #     for i in reversed(range(0, ind)):
        #         if not popped[i]:
        #             return i
        #     return -1

        # def get_r(ind):
        #     for i in range(ind + 1, n):
        #         if not popped[i]:
        #             return i
        #     return -1

        # def rec():
        #     v = 0
        #     for i in range(n):
        #         if popped[i]:
        #             continue
        #         l = get_l(i)
        #         r = get_r(i)
        #         M = nums[i]
        #         L = 1 if l == -1 else nums[l]
        #         R = 1 if r == -1 else nums[r]
        #         popped[i] = True
        #         v = max(v, rec() + L * M * R)
        #         popped[i] = False
        #     return v
    
        # return rec()