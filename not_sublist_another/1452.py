class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        
        #brute force
        s = [set(cs) for cs in favoriteCompanies]
        ans = []
        l = len(favoriteCompanies)
        for i, l1 in enumerate(s):
            notsubset = True
            for j, l2 in enumerate(s):
                if i != j and l1.issubset(l2):
                    notsubset = False
            if notsubset:
                ans.append(i)
        return ans