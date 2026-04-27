class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [0] * numCourses
        out = []
        counter = 0
        d = defaultdict(list)
        for i, prereq in prerequisites:
            d[prereq].append(i)

        def dfs(i):
            nonlocal counter
            if visited[i] == 2:
                return False
            if visited[i] == 1:
                return True # has cycle
            visited[i] = 1
            for next_i in d[i]:
                if dfs(next_i):
                    return True # has cycle

            out.append(i)
            visited[i] = 2
            return False
        
        for i in range(numCourses):
            if dfs(i):
                return []

        out.reverse()
        return out