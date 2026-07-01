class SparseVector:
    def __init__(self, nums: List[int]):
        self.pairs = []
        for i in range(len(nums)):
            if nums[i] != 0:
                self.pairs.append((i, nums[i]))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        i, j = 0, 0
        res = 0
        while i < len(self.pairs) and j < len(vec.pairs):
            i_ind, i_val = self.pairs[i]
            j_ind, j_val = vec.pairs[j]
            if i_ind < j_ind:
                i += 1
            elif i_ind > j_ind:
                j += 1
            else:
                res += i_val * j_val
                i += 1
                j += 1
        return res


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
