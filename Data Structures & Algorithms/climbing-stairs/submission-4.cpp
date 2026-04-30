class Solution {
public:
    int climbStairs(int n) {
        return this->rec(0, n);
    }

private:
    int rec(int k, int n) {
        if (k == n) return 1;
        if (k > n) return 0;
        return this->rec(k + 1, n) + this->rec(k + 2, n);
    }
};
