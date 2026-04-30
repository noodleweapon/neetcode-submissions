class Solution {
    /**
     * @param {number} n
     * @return {string[]}
     */
    generateParenthesis(n) {
        const res = [];
        rec(1, 0, n, '(', res);
        return res;
    }

    rec(open, close, n, seq, res) {
        if (open < n) rec(open + 1, close, seq + '(', res);
        if (close < open) rec(open, close + 1, seq + ')', res);
        if ((open == n) && (close == n)) res.push(seq);
    }
}
