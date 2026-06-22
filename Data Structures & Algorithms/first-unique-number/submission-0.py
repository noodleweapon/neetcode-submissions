class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.f = defaultdict(int)
        self.ptr = {}

        self.left = ListNode(-1)
        self.right = ListNode(-1)
        self.left.next, self.right.prev = self.right, self.left
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        return self.left.next.val

    def add(self, value: int) -> None:
        self.f[value] += 1

        if self.f[value] == 2:
            node = self.ptr[value]
            l, r = node.prev, node.next
            l.next, r.prev = r, l
            del self.ptr[value]
        elif self.f[value] == 1:
            l = self.right.prev
            node = ListNode(value)
            l.next = self.right.prev = node
            node.prev, node.next = l, self.right
            self.ptr[value] = node


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
