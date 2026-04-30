class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def rec(self, i, d, seen):
        if not d[i]:
            return True
        seen.add(i)
        for prereq in d[i]:
            if prereq == i:
                continue
            if prereq in seen:
                return False
            if not self.rec(prereq, d, seen):
                return False
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(set)
        for course, prereq in prerequisites:
            d[course].add(prereq)
        
        for i in range(numCourses):
            if not self.rec(i, d, set()):
                return False
        return True