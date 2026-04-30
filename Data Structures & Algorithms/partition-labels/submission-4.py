class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}
        res = []
        start = 0
        end = 0
        for i, c in enumerate(s):
            if i == end:
                res.append(end - start + 1)
                start = i + 1
            end = max(last[c], end)
        return res