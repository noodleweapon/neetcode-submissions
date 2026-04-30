class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(key=lambda x: x[0], reverse=True)
        stack = []

        for car in cars:
            time = (target - car[0]) / car[1]
            while stack and stack[-1] >= time:
                stack.pop()
            stack.append(time)
        
        return len(stack)