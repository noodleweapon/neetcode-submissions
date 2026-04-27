from collections import deque
class Solution:
    def is_subset(self, sd, td):
        for k, v in td.items():
            sdv = sd[k]
            if sdv < v:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        td = Counter(t)
        best_s = ""
        sd = defaultdict(int)
        q = deque([])
        for i, c in enumerate(s):
            q.append(c)
            sd[c] += 1

            while q and sd[q[0]] - td[q[0]] > 0:
                qc = q.popleft()
                sd[qc] -= 1

            if self.is_subset(sd, td):
                if best_s == "" or (len(best_s) > len(q)):
                    best_s = "".join(q)
        
        return best_s
