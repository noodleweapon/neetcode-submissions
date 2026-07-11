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
        # MISTAKE 2: I was using append + sort instead of just insert.
        if R != endTime:
            self.free.insert(l, (endTime, R))
        if L != startTime:
            self.free.insert(l, (L, startTime))
        return True

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)