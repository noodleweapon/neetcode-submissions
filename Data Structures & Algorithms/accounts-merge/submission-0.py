class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        rank = {}
        res = {}

        def find_parent(email):
            if parent[email] != email:
                parent[email] = find_parent(parent[email])
            return parent[email]
        
        def add(name, email):
            if email not in parent:
                parent[email] = email
                rank[email] = 1
                res[email] = (name, [email])

        def union(a, b):
            par_a = find_parent(a)
            par_b = find_parent(b)
            if par_a == par_b:
                return
            if rank[par_a] > rank[par_b]:
                parent[par_b] = par_a
                rank[par_a] += rank[par_b]
                for email in res[par_b][1]:
                    res[par_a][1].append(email)
                del res[par_b]
            else:
                parent[par_a] = par_b
                rank[par_b] += rank[par_a]
                for email in res[par_a][1]:
                    res[par_b][1].append(email)
                del res[par_a]

        nameD = {}

        for account in accounts:
            name = account[0]
            emails = account[1:]
            for email in emails:
                add(name, email)
            
            for i in range(len(emails) - 1):
                union(emails[i], emails[i + 1])
        
        output = []
        for record in res.values():
            name, emails = record
            emails.sort()
            output.append([name, *emails])
        return output


        # definitely belong to the same person if there is some common email to both accounts
        # all of their accounts definitely have the same name (just a fact, so i don't have to worry about same email and diff name scenario)