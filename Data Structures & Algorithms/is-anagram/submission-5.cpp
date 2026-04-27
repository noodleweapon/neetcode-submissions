class Solution {
public:
    bool isAnagram(string s, string t) {
        const int n = s.size();
        std::unordered_map<char, int> S;
        for (int i = 0; i < n; i++) S[s[i]] += 1;
        for (char c : t) S[c] -= 1;

        for (const auto& [k, v] : S) {
            if (v != 0) return false;
        }
        return true;
    }
};
