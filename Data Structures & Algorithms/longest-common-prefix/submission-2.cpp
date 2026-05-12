class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 1) return strs[0];
        const string& s = strs[0];
        for (int i = 0; i < s.size(); i++) {
            const char& c = s[i];
            for (int j=1; j < strs.size(); j++) {
                if (i >= strs[j].size()) return s.substr(0, i);
                const char& t = strs[j][i];
                if (c != t) return s.substr(0, i);
            }
        }
        return s;
    }
};

        // if len(strs) == 1:
        //     return strs[0]
        
        // for i, c in enumerate(strs[0]):
        //     for s in strs[1:]:
        //         if i >= len(s) or s[i] != c:
        //             return s[:i]
        // return strs[0]