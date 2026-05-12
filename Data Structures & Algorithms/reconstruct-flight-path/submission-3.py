class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)

        route = []

        def dfs(src):
            while graph[src]:
                dfs(graph[src].pop())
            route.append(src)

        dfs("JFK")
        return route[::-1]