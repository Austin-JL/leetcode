class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda k: (k[0], -k[1]), reverse=True)
        # ie : [7,1] -> [7,-1] sort value in decending order; revers=True sort key in deecending order
        new_people = []
        for p in people :
            new_people.insert(p[1],p)
        return new_people