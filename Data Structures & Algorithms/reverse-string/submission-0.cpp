#include <cmath>

class Solution {
public:
    void reverseString(vector<char>& s) {
        const int n = s.size();
        const int mid = floor(n / 2);
        for (int i=0; i<mid; i++) {
            const char tmp = s[n - 1 - i];
            s[n - 1 - i] = s[i];
            s[i] = tmp;
        }
    }
};