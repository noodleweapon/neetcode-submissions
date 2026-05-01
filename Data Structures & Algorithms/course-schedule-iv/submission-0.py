class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        d = defaultdict(list)
        for prereq, course in prerequisites:
            d[prereq].append(course)
        
        def dfs(visited, prereq, finding):
            visited.add(prereq)
            if prereq == finding:
                return True
            for course in d[prereq]:
                if course not in visited:
                    if dfs(visited, course, finding):
                        return True
            return False

        answer = [] # future course, found future course.
        for prereq, course in queries:
            answer.append(dfs(set(), prereq, course))
        return answer