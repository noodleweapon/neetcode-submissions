class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        rem_groups = len(hand) // groupSize
        hand.sort()
        h = []
        for i, v in enumerate(hand):
            if h and h[0] == v:
                heapq.heappop(h)
            else:
                if rem_groups == 0:
                    return False
                rem_groups -= 1
                for i in range(1, groupSize):
                    heapq.heappush(h, v + i)
        return True

        # [1, 2, 2, 3, 3, 4, 6, 7, 8]
        # [1, 2, 2, 3, 3, 4, 6, 7, 8]


        2,3
        3,4
        7,8

