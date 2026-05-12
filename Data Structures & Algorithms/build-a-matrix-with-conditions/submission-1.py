class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def get_order(conditions):
            g = defaultdict(list)
            visit = [0] * (k + 1)
            order = []
            for a, b in conditions:
                g[b].append(a)
            
            def dfs(u):
                if visit[u] == 1:
                    return True # has cycle
                visit[u] = 1
                for v in g[u]:
                    if visit[v] != 2: # visited
                        if dfs(v):
                            return True
                visit[u] = 2
                order.append(u)
                return False
            
            for u in range(1, k + 1):
                if visit[u] == 0:
                    if dfs(u):
                        return None # has cycle
            return order
        
        row_order = get_order(rowConditions)
        if not row_order: # [2,1,3]
            return []
        col_order = get_order(colConditions)
        if not col_order: # [2,3,1]
            return []
                
        res = []
        for r in range(k):
            new_row = []
            for c in range(k):
                new_row.append(0)
                if row_order[r] == col_order[c]:
                    new_row[-1] = row_order[r]
            res.append(new_row)
        return res
        



        # [2,0,0]
        # [0,0,1]
        # [0,3,0]

        # Row:
        # [2,1],[1,3]
        # - 2 is above 1
        # - 1 is above 3

        # Col:
        # [3,1],[2,3]
        # - 3 is left of 1
        # - 2 is left of 3