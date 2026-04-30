class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums) {
        for (let i=0; i<nums.length; i++) {
            const ni = i == nums.length - 1 ? 0 : i + 1;
            const v = nums[i]
            const nv = nums[ni]
            if (nv < v) {
                return nv
            }
        }
    }
}
