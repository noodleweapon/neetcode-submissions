from collections import defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        fs = [0] * 26
        for task in tasks:
            fs[ord(task) - ord("A")] += 1
        fs.sort()
        buckets = [0] * (n + 1)

        while fs:
            f = fs.pop()
            buckets.sort()
            buckets[0] += f

        bucketMax = max(buckets)
        emptyTop = 0
        for bucket in buckets:
            if bucket < bucketMax:
                emptyTop += 1
        return bucketMax * (n + 1) - emptyTop




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
        