class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for p, s in zip(position, speed):
            t = (target - p) / s
            pairs.append((p, t))
        pairs.sort(key = lambda x : x[0], reverse=True)

        stack = []
        for pair in pairs:
            stack.append(pair)
            if len(stack) >= 2 and stack[-2][1] >= stack[-1][1]:
                stack.pop()
        
        return len(stack)