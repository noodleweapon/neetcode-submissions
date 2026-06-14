class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        d = collections.defaultdict(set)
        for a, b in edges:
            d[a].add(b)
            d[b].add(a)
        
        leaves = []
        for i in range(n):
            if len(d[i]) == 1:
                leaves.append(i)
        
        removed = 0
        while n - removed > 2:
            removed += len(leaves)
            new_leaves = []
            for leaf in leaves:
                parent = next(iter(d[leaf]))
                d[leaf].remove(parent)
                d[parent].remove(leaf)
                if len(d[parent]) == 1:
                    new_leaves.append(parent)
            
            leaves = new_leaves

        return leaves