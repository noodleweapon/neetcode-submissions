class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        counter = Counter(hand)
        hand.sort()
        for i, v in enumerate(hand):
            if counter[v] == 0:
                continue
            for j in range(1, groupSize):
                counter[v + j] -= counter[v]
                if counter[v + j] < 0:
                    return False
            counter[v] = 0
        
        return True