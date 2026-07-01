class SparseVector:
    def __init__(self, nums: List[int]):
        self.inds = set()
        self.nums = nums
        self.n = len(nums)
        for i in range(self.n):
            if nums[i] != 0:
                self.inds.add(i)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for ind in self.inds:
            res += self.nums[ind] * vec.nums[ind]
        return res


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
