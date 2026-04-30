class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        counter = Counter(hand)
        hand.sort()
        for i, v in enumerate(hand):
            if counter[v] == 0:
                continue
            if counter[v] < 0:
                return False
            for j in range(groupSize):
                counter[v + j] -= 1
        
        return True