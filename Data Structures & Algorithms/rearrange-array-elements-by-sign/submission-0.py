class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        P = deque([])
        N = deque([])
        i = j = 0
        while i < len(nums):
            want_pos = i % 2 == 0
            while True:
                if want_pos:
                    if P:
                        nums[i] = P.popleft()
                        break
                else:
                    if N:
                        nums[i] = N.popleft()
                        break
                
                if j >= len(nums):
                    break
                num = nums[j]
                if num > 0:
                    P.append(num)
                elif num < 0:
                    N.append(num)
                j += 1
            i += 1
        return nums





