class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        n = len(arrival)
        enter = deque()
        exit = deque()
        i = 0
        for t, way in zip(arrival, state):
            if way == 0:
                enter.append((i, t))
            else:
                exit.append((i, t))
            i += 1
        t = 0
        prev = -1
        seconds = [-1] * n
        while enter or exit:
            hasEnter = enter and enter[0][1] <= t # I HAD THIS BACKWARDS
            hasExit = exit and exit[0][1] <= t
            if hasEnter and hasExit:
                if prev == 0:
                    seconds[enter.popleft()[0]] = t
                    prev = 0
                else:
                    seconds[exit.popleft()[0]] = t
                    prev = 1
                t += 1
                continue
            
            if hasEnter:
                seconds[enter.popleft()[0]] = t
                prev = 0
                t += 1
            elif hasExit:
                seconds[exit.popleft()[0]] = t
                prev = 1
                t += 1
            else:
                options = []
                if enter:
                    options.append(enter[0][1])
                if exit:
                    options.append(exit[0][1])
                prev = -1
                t = min(options)
        return seconds

        # state:
        # 1 = enter
        # 0 = exit
        # -1 = UNUSED
        # arrival (len = n), non decreasing

        # prev = -1


