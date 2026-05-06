class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D_kills = 0
        R_kills = 0
        last_kill = senate[0]
        ongoing = True
        alive = [True] * len(senate)
        while ongoing:
            ongoing = False
            for i, c in enumerate(senate):
                if not alive[i]:
                    continue
                if c == 'R':
                    if D_kills > 0:
                        D_kills -= 1
                        alive[i] = False
                        last_kill = 'Dire'
                        ongoing = True
                    else:
                        R_kills += 1
                elif c == 'D':
                    if R_kills > 0:
                        R_kills -= 1
                        alive[i] = False
                        last_kill = 'Radiant'
                        ongoing = True
                    else:
                        D_kills += 1

        return last_kill