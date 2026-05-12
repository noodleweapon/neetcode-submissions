class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])
        i1 = i2 = 0
        n1, n2 = len(slots1), len(slots2)
        while i1 < n1 and i2 < n2:
            s1, s2 = slots1[i1], slots2[i2]

            # case 1: Doesn't overlap
            if s1[1] <= s2[0]:
                i1 += 1
                continue
            if s2[1] <= s1[0]:
                i2 += 1
                continue

            s = max(s1[0], s2[0])
            t = min(s1[1], s2[1])
            if t - s >= duration:
                return [s, s + duration]

            # Case 2: Overlaps but not enough.
            if s1[1] < s2[1]:
                i1 += 1
            elif s2[1] < s1[1]:
                i2 += 1
            else:
                i1 += 1
                i2 += 1


        return []

        # slots1=[[200,300],[50,100],[10,30]]
        # slots2=[[250,350],[80,120],[25,60]]
        # duration=15

            
        

        # [10,15],[12,120],[140,210]
        # [14,300],[60,70]


