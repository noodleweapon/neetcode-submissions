class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        bold_intervals = []
        for word in words:
            i = -1
            while True:
                i = s.find(word, i + 1)
                if i == -1:
                    break
                bold_intervals.append([i, i + len(word)])
        bold_intervals.sort()
        bolds = []
        for bold_interval in bold_intervals:
            if bolds and bolds[-1][1] >= bold_interval[0]:
                bolds[-1][1] = max(bolds[-1][1], bold_interval[1])
            else:
                bolds.append(bold_interval)
        res = list(s)
        for i in reversed(range(len(bolds))):
            o, c = bolds[i]
            res.insert(c, '</b>')
            res.insert(o, '<b>')
        return "".join(res)