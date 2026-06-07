class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 30,38,30,36,35,40,28
        # 1,4,1,2,1,0,0
        
        # s = [40, 35]

        n = len(temperatures)
        s = []
        res = [0] * n
        for i in reversed(range(n)):
            T = temperatures[i]
            while s and temperatures[s[-1]] <= T:
                s.pop()
            if s:
                res[i] = s[-1] - i
            s.append(i)
        return res