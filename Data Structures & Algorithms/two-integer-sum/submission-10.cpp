#include <algorithm> // std::sort
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        using namespace std;
        vector<pair<int, int>> pairs;
        for (int i = 0; i < nums.size(); i ++) {
            pairs.push_back({nums[i], i});
        }
        sort(pairs.begin(), pairs.end(), [](const auto& a, const auto& b) {
            return a.first < b.first;
        });
        int i = 0;
        int j = pairs.size() - 1;
        while (i < j) {
            const int s = pairs[i].first + pairs[j].first;
            if (s > target) {
                j -= 1;
            } else if (s < target) {
                i += 1;
            } else {
                break;
            }
        }
        vector<int> m = {pairs[i].second, pairs[j].second};
        sort(m.begin(), m.end());
        return m;
    }
};
