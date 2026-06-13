class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for course, prereq in prerequisites:
            d[course].append(prereq)
        res = []
        visit = [0] * numCourses
        def has_cycle(i):
            if visit[i] == 2:
                return False
            if visit[i] == 1:
                return True
            visit[i] = 1
            for j in d[i]:
                if has_cycle(j):
                    return True
            visit[i] = 2
            res.append(i)
            return False

        for i in range(numCourses):
            if has_cycle(i):
                return []
        return res
