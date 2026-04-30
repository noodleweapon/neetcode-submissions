#include <algorithm> // std::sort
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::sort(nums.begin(), nums.end());
        int i = 0;
        int j = nums.size() - 1;
        while (i < j) {
            const int s = nums[i] + nums[j];
            if (s > target) {
                j -= 1;
            } else if (s < target) {
                i += 1;
            } else {
                break;
            }
        }
        vector<int> m = {i, j};
        return m;
    }
};
