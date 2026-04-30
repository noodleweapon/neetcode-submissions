class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = Counter(tasks)
        h = []
        for c in d.keys():
            print(c)
        return 0