class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        heads = len(hand) // groupSize
        hand.sort()
        h = []
        for i, v in enumerate(hand):
            if h and h[0] == v:
                heapq.heappop(h)
            elif h and h[0] < v:
                return False
            else:
                if heads == 0:
                    return False
                heads -= 1
                heapq.heappush(h, v + 1)
                heapq.heappush(h, v + 2)
                heapq.heappush(h, v + 3)
        print(len(h), heads)
        return len(h) == 0