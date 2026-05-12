class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        let V = 0;
        let li = 0;
        let ri = height.length - 1;
        let H = 0;
        while (li < ri) {
            const lh = height[li];
            const rh = height[ri];
            if (lh < H) V += H - lh;
            if (rh < H) V += H - rh;
            const h = Math.min(lh, rh);
            if (h > H) H = h;
            if (lh < rh) {
                li += 1
            } else {
                ri -= 1
            }
        }
        return V
    }
}
