class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        h = []
        for stick in sticks:
            heapq.heappush(h, stick)
        
        cost = 0
        while len(h) >= 2:
            a, b = heapq.heappop(h), heapq.heappop(h)
            c = a + b
            cost += c
            heapq.heappush(h, c)

        return cost


        # 2+4,3

        # 6+3=9
        # 6+9 = 15

        # [1,8,3,5]
        # 1+3 = 4
        # [4,8,5]
        # 4 + 5 = 9
        # [9, 8]
        # 9 + 8 = 

        # [a+b+c]
        # (a+b)*2+c

        # [a+b+c+d]
        # [(a+b), c, d]
        # Cost: a+b
        # [(a + b + c), d]
        # Cost: a + b + (a + b) + c