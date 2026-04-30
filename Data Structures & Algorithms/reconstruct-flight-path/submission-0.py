class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        N = len(tickets)
        d = defaultdict(list)
        for src, dst in tickets:
            d[src][dst] = False