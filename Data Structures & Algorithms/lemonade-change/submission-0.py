class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            c[bill] += 1
            
            if bill >= 10:
                if c[5] == 0:
                    return False
                c[5] -= 1
            
            if bill == 20:
                if c[10] >= 1:
                    c[10] -= 1
                elif c[5] >= 2:
                    c[5] -= 2
                else:
                    return False

        return True