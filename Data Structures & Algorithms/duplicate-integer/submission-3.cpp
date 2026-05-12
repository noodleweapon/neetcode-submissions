#include <unordered_map>
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> d;
        for (const int& num : nums) {
            if (d.count(num)) return true;
            d[num] = 1;
        }
        return false;
    }
};