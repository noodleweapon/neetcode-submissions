class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for p, s in zip(position, speed):
            t = (target - p) / s
            stack.append((p, t))
        
        stack.sort(key = lambda x : x[0], reverse=True)
        
        count = 0
        while len(stack) >= 2:
            front, back = stack[-2], stack[-1]
            if front[1] >= back[1]:
                stack.pop()
                stack.pop()
                stack.append(back)
            else:
                stack.pop()
                count += 1
            
            print("l", stack, count)

        print(count)
        return len(stack) + count