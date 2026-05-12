class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [0] * numCourses
        post = [-1] * numCourses
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

            counter += 1
            post[i] = counter
            visited[i] = 2
            return False
        
        for i in range(numCourses):
            if dfs(i):
                return []
        

        h = []
        for i, p in enumerate(post):
            heapq.heappush(h, (-p, i))
        
        out = []
        while h:
            out.append(heapq.heappop(h)[1])
        return out