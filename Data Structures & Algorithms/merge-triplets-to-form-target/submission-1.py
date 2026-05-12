class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a = b = c = float("-inf")
        [A, B, C] = target
        for x, y, z in triplets:
            if x > A or y > B or z > C:
                continue
            a = max(a, x)
            b = max(b, y)
            c = max(c, z)
        return a == A and b == B and c == C