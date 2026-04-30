class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        N = len(tickets)
        nxtmap = defaultdict(list)
        visited = defaultdict(list)
        for src, dst in tickets:
            nxtmap[src].append(dst)
            nxtmap[src].sort()
            visited[src].append(False)
        
        
        output = []
        def dfs(src, n, path):
            nonlocal output
            if n == 0:
                if len(output) == 0:
                    output = path.copy()
                return
            
            for i in range(len(visited[src])):
                if visited[src][i]:
                    continue
                nxt = nxtmap[src][i]
                visited[src][i] = True
                path.append(nxt)
                dfs(nxt, n - 1, path)
                path.pop()
                visited[src][i] = False

        dfs("JFK", N, ["JFK"])
        return output