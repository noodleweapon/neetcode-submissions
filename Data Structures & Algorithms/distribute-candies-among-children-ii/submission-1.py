class Solution:
    def distributeCandies(self, candies: int, limit: int) -> int:
        if candies > limit * 3:
            return 0

        res = 0
        for a in range(limit + 1):
            need = candies - a
            bMin = max(0, need - limit)
            bMax = min(limit, need)
            res += max(0, bMax - bMin + 1)
        return res

        
            





        # res = 0
        # for a in range(limit + 1):
        #     for b in range(a + 1, limit + 1):
        #         cRange = [b + 1, limit]
        #         res += (cRange[1] - cRange[0] + 1) * 6
        #     cRange = [a + 1, limit]
        #     res += (cRange[1] - cRange[0] + 1) * 3
        # if n % 3 == 0:
        #     if n // 3 <= limit:
        #         res += 1
        # return res

        # 1,2,x --> 2 * 3 ways
        # 1,1,x --> 1 * 3 way

        # 1,1,1, etc...