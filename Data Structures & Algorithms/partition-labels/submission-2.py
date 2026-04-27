class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i, c in enumerate(s):
            if c in d:
                d[c] = (d[c][0], i)
            else:
                d[c] = (i, i)

        arr = list(d.values())
        arr.sort(key=lambda x: x[0])
        res = []

        start = arr[0][0]
        end = arr[0][1]
        for i in range(1, len(arr)):
            if arr[i][0] > end:
                res.append(end - start + 1)
                start = arr[i][0]
                end = arr[i][1]
            else:
                end = max(arr[i][1], end)
        res.append(end - start + 1)
        return res