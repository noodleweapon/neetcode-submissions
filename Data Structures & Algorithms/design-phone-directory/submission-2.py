class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.free = [v for v in range(maxNumbers)]
        self.used = set()

    def get(self) -> int:
        if self.free:
            v = self.free.pop()
            self.used.add(v)
            return v
        else:
            return -1

    def check(self, number: int) -> bool:
        return number not in self.used

    def release(self, number: int) -> None:
        if number not in self.used:
            return
        self.used.remove(number)
        self.free.append(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
