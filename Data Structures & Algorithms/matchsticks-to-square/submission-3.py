class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        matchsticks.sort(reverse=True)
        side = total // 4
        if side * 4 != total:
            return False
        
        seen = set()
        def rec(i, items):
            if i == len(matchsticks):
                for j in range(4):
                    if items[j] != side:
                        return False
                return True

            v = matchsticks[i]
            for j in range(4):
                items[j] += v
                tup = (i + 1, *sorted(items))
                if (tup not in seen) and (items[j] <= side):
                    seen.add(tup)
                    if rec(i + 1, items):
                        return True
                items[j] -= v
            return False
            
        return rec(0, [0,0,0,0])

        
        # side 5
        # 3, 1,1
        # 4, 2
        # --> fail.



        # 1+3
        # 4
        # 2+2
        # 4


        # 1,5,6,4
        # 6+6+4 = 16, side 4.