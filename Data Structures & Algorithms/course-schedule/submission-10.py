class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)
        for i, prereq in prerequisites:
            d[i].append(prereq)
        
        visited = [False] * numCourses
        visiting = [False] * numCourses
        def has_cycle(i):
            if visiting[i]:
                return True
            visiting[i] = True

            for prereq in d[i]:
                if visited[prereq]:
                    continue
                if has_cycle(prereq):
                    return True
            
            visiting[i] = False
            visited[i] = True
                
        for i in range(numCourses):
            if visited[i]:
                continue
            if has_cycle(i):
                return False
        return True
