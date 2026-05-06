class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
        
        maxReach = maxJump
        minReach = minJump

        for i, c in enumerate(s):
            if i < minReach:
                continue
            if i > maxReach:
                return False
            if c == '1':
                continue
            maxReach = max(maxReach, i + maxJump)
            # minReach = i + minReach
            
        return True



        # 00110010
        #   a   a
        # 01234567
