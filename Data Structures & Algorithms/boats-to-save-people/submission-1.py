class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        l, r = 0, n - 1
        res = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            elif people[r] <= limit:
                r -= 1
            res += 1
        return res

        # 5,1,4,2
        # 1,2,4,5
        # 1,2,3,3,4