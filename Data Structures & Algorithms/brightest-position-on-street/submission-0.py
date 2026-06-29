class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        arr = []
        for pos, rad in lights:
            arr.append([pos - rad, pos + rad])
        arr.sort()

        h = [] # right edge
        brightness = 0
        res, maxB = -1, float("-inf")
        for l, r in arr:
            heapq.heappush(h, r)
            brightness += 1
            while h and h[0] < l:
                heapq.heappop(h)
                brightness -= 1
            
            if brightness > maxB:
                maxB = brightness
                res = l
        return res