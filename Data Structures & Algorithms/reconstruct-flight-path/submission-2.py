class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        N = len(tickets)
        nxtmap = defaultdict(list)
        visited = defaultdict(list)
        for src, dst in tickets:
            nxtmap[src].append(dst)
            visited[src].append(False)
        
        for src, arr in nxtmap.items():
            arr.sort()
        
        path = ["JFK"]
        def dfs(src, n):
            if n == 0:
                return True
            for i in range(len(visited[src])):
                if visited[src][i]:
                    continue
                nxt = nxtmap[src][i]
                visited[src][i] = True
                path.append(nxt)
                if dfs(nxt, n - 1):
                    return True
                path.pop()
                visited[src][i] = False
            return False

        dfs("JFK", N)
        return path