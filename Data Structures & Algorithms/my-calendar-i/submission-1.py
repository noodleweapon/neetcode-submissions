class MyCalendar:
    
    def __init__(self):
        self.free = [(0, float("inf"))]

    def book(self, startTime: int, endTime: int) -> bool:
        l, r = 0, len(self.free) - 1
        while l < r:
            m = (l + r + 1) // 2
            if self.free[m][0] <= startTime:
                # MISTAKE: I had it reversed.
                l = m
            else:
                r = m - 1
        
        L, R = self.free[l]
        if not (L <= startTime and endTime <= R):
            return False

        self.free.pop(l)
        if L != startTime:
            self.free.append((L, startTime))
        if R != endTime:
            self.free.append((endTime, R))
        self.free.sort()
        return True

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)