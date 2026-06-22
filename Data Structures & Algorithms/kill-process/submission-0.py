class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        E = defaultdict(set)
        for myID, parID in zip(pid, ppid):
            if parID == 0:
                continue
            E[parID].add(myID)
        
        killed = set()
        def dfs(u):
            if u in killed:
                return
            killed.add(u)
            for v in E[u]:
                dfs(v)

        dfs(kill)
        return list(killed)