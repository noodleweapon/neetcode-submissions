class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        # every number is either in dict (in use) or stack (free)
        self.stack = [v for v in range(maxNumbers)]
        self.dict = {}

    def get(self) -> int:
        if self.stack:
            v = self.stack.pop()
            self.dict[v] = True
            return v
        else:
            return -1

    def check(self, number: int) -> bool:
        return number not in self.dict

    def release(self, number: int) -> None:
        if number not in self.dict:
            return
        del self.dict[number]
        self.stack.append(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
