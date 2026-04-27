class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        const int n = nums.size();
        int k = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (nums[i] != val) continue;
            nums.erase(nums.begin() + i);
            k ++;
        }
        return n - k;
    }
};