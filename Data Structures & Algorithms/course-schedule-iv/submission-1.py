class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ps = [None for _ in range(numCourses)]
        d = defaultdict(list)
        for u, v in prerequisites:
            d[v].append(u)

        def get_ps(i):
            if ps[i] != None:
                return ps[i]

            arr = set()
            for j in d[i]:
                arr_2 = get_ps(j)
                arr.update(arr_2)
                arr.add(j)
            ps[i] = arr
            return arr

        for i in range(numCourses):
            ps[i] = get_ps(i)

        return [u in ps[v] for u, v in queries]