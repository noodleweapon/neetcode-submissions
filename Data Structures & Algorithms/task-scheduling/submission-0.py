from collections import defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        fs = [0] * 26
        for task in tasks:
            fs[ord(task) - ord("a")] += 1
        fs.sort(reverse=True)


        # d = defaultdict(int)
        # maxV = None
        # maxC = 0
        # totC = 0
        # for task in tasks:
        #     d[task] += 1
        #     totC += 1
        #     newC = d[task]
        #     if maxC > newC:
        #         continue
        #     maxC = newC
        #     maxV = task
        
        # etcC = totC - maxC

        # mainLength = (maxC - 1) * (n + 1) + 1
        # slotsBetween = mainLength - maxC
        # slotsAtEnd = max(0, etcC - slotsBetween)
        # print(mainLength, slotsAtEnd)
        # return mainLength + slotsAtEnd
        