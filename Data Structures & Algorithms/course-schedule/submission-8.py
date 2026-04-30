class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)
        for i, prereq in prerequisites:
            d[prereq].append(i)
        
        def has_cycle(i, seen):
            seen.add(i)
            for j in d[i]:
                if j in seen:
                    return True
                if has_cycle(j, seen):
                    return True
            return False
        
        for i in range(numCourses):
            if has_cycle(i, set()):
                return False
        return True
        
        
        # d = {}
        # for i, prereq in prerequisites:
        #     d[i] = prereq
        
        # cycle = [True] * numCourses
        # def has_cycle(i):
        #     if not cycle[i]:
        #         return False
        #     if i not in d:
        #         return False
        #     return has_cycle(d[i])
