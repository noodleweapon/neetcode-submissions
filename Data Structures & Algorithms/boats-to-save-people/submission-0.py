class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0
        while l <= r:
            if l == r:
                boats += 1
                break
            if people[l] + people[r] > limit:
                boats += 1
                r -= 1
            else:
                boats += 1
                l += 1
                r -= 1
        return boats

        # weight = 3
        # 1,3,2,3,2
        # 1, 2, 2, 3, 3
        
        # weight = 6
        # people = [2,3,5]

        # limit = 6
        # people = [1,1,1]