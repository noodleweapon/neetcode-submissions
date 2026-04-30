class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        n = nums.size()
        vector<int> res;
        res.reserve(2 * n);
        for (const int& num : nums) {
            res.push_back(num);
        }
        for (const int& num : nums) {
            res.push_back(num);
        }
        return res;
    }
};