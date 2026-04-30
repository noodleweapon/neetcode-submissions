class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        const res = {}
        for (let i = 1; i < nums.length - 1; i ++) {
            let li = i - 1;
            let ri = i + 1;
            const target = -nums[i];
            while ((li >= 0) && (ri < nums.length)) {
                const sum = nums[li] + nums[ri];
                if (sum == target) {
                    res[[li, i, ri]] = true;
                    break;
                }
                if (sum < target) {
                    ri++;
                } else {
                    li--;
                }
            }
        }
        return Object.keys(res)
    }
}
