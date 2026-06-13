class UF:
    def __init__(self, n, names, emails):
        self.rank = [1] * n
        self.par = [i for i in range(n)]
        self.names = names
        self.emails = emails
    
    def find(self, i):
        if self.par[i] != i:
            self.par[i] = self.find(self.par[i])
        return self.par[i]
        
    def union(self, a, b):
        A, B = self.find(a), self.find(b)
        if A == B:
            return False
        if self.rank[A] > self.rank[B]:
            self.rank[A] += self.rank[B]
            self.rank[B] = 0
            self.emails[A] |= self.emails[B]
            self.emails[B] = []
            self.par[B] = A
        else:
            self.rank[B] += self.rank[A]
            self.rank[A] = 0
            self.emails[B] |= self.emails[A]
            self.emails[A] = []
            self.par[A] = B
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        names = list(map(lambda x: x[0], accounts))
        emails = list(map(lambda x: set(x[1:]), accounts))
        uf = UF(n, names, emails)
        emailDict = {}
        for i in range(n):
            for email in accounts[i][1:]:
                if email in emailDict and emailDict[email] != i:
                    uf.union(emailDict[email], i)
                emailDict[email] = i

        res = []
        for i in range(n):
            if uf.rank[i] > 0:
                res.append([uf.names[i]] + list(sorted(uf.emails[i])))

        return res