class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights) # would be at most len(weights) days
        r = l * days # would be 1 day.

        def works(cap):
            t = d = 0 # if no weights, gives 0 days.
            for w in weights:
                if t - w < 0:
                    t = cap - w
                    d += 1
                else:
                    t -= w
            return d <= days

        working_m = r
        while l <= r:
            m = (l + r) // 2
            if works(m):
                print(m)
                working_m = m
                r = m - 1
            else:
                l = m + 1
        
        return working_m

        # weights=[1,5,  4,4,  2,3]
        # days=3

        # 7





        # 1,1,1,1,1,1,1,1
        
        # 2,4,6,1,3,10

        # 2+4 = 6, 6+1+3 = 10, 10 = 3 days

        # If 9,

        # 2+4=6, 6+1=7, 3, 10!!!