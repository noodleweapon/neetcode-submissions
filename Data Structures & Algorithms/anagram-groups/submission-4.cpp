#include <unordered_map>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> m;
        for (const auto& str : strs) {
            string b = str;
            sort(b.begin(), b.end());
            if (!m.count(b)) m[b] = {};
            m[b].push_back(str);
        }
        vector<vector<string>> res;
        for (const auto& [k, v] : m) {
            res.push_back(v);
        }
        return res;
    }
};
