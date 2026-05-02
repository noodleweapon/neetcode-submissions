class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R = deque([])
        D = deque([])

        for i, c in enumerate(senate):
            if c == 'R':
                R.append(i)
            else:
                D.append(i)
        
        while R and D:
            r = R.popleft()
            d = D.popleft()
            if r < d:
                R.append(r + len(senate))
            else:
                D.append(d + len(senate))
        
        if R:
            return 'Radiant'
        else:
            return 'Dire'