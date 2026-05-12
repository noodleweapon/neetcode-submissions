class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
        
        reach = [False] * len(s)
        reach[0] = True

        for i, c in enumerate(s):
            if not reach[i]:
                continue
            if c == '1':
                continue
            for j in range(i + minJump, min(i + maxJump + 1, len(s))):
                reach[j] = True
        return reach[len(s) - 1]



        # 00110010
        #   a   a
        # 01234567
