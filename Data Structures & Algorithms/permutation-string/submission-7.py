class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        C1 = Counter(s1)
        C2 = defaultdict(int)
        for i in range(len(s2)):
            C2[s2[i]] += 1
            if i >= n:
                C2[s2[i - n]] -= 1

            all_same = True
            for z in C1:
                if C2[z] != C1[z]:
                    all_same = False
                    break

            if all_same:
                return True
        return False
