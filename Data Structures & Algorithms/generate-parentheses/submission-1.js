class Solution {
    /**
     * @param {number} n
     * @return {string[]}
     */
    generateParenthesis(n) {
        const res = [];
        this.rec(n, 1, 0, '(', res);
        return res;
    }

    rec(n, open, close, seq, res) {
        if (open < n) this.rec(n, open + 1, close, seq + '(', res);
        if (close < open) this.rec(n, open, close + 1, seq + ')', res);
        if ((open == n) && (close == n)) res.push(seq);
    }
}
