class Solution:
    def isNStraightHand(self, hands: List[int], groupSize: int) -> bool:
        hands.sort()
        groups = [[] for _ in range(len(hands) // groupSize)]
        for hand in hands:
            didAdd = False
            for group in groups:
                if len(group) >= groupSize:
                    continue
                if not group or group[-1] == hand - 1:
                    group.append(hand)
                    didAdd = True
                    break
            if not didAdd:
                return False
        return True
