class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ta, tb, tc = target
        ba = bb = bc = False
        for i, triplet in enumerate(triplets):
            ia, ib, ic = triplet
            if ia > ta or ib > tb or ic > tc:
                continue
            if ia == ta:
                ba = True
            if ib == tb:
                bb = True
            if ic == tc:
                bc = True
        return ba and bb and bc