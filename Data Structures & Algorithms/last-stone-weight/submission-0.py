import heapq

class Solution:
    def smash(self, a, b):
        if a > b:
            return [a - b, 0]
        if b > a:
            return [0, b - a]
        return [0, 0]

    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) < 2:
            stones.extend([0, 0])
        heapq.heapify(stones)
        while True:
            a, b = heapq.nlargest(2, stones)
            if a == 0 or b == 0:
                return a

            smash_res = self.smash(a, b)
            stones[0] = smash_res[0]
            stones[1] = smash_res[1]