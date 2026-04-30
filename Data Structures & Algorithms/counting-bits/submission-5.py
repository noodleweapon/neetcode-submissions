class Solution:
    def countBits(self, n: int) -> List[int]:
        if n <= 2:
            return [n]
        arr = [0, 1]
        for i in range(2, n + 1):
            z = 0
            num = i
            for j in range(i.bit_length()):
                if num & 1 == 1:
                    z += 1
                num = num >> 1
            arr.append(z)
        return arr