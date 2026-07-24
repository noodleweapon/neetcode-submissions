class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # think: I can also go in reverse
        target.append(0)

        res = 0
        stack = []
        for num in target:
            M = num
            while stack and stack[-1] > num:
                M = max(M, stack.pop())
            res += M - num

            if (not stack) or (stack[-1] < num):
                stack.append(num)
        return res

        3,1,5,4,2,3,4,2