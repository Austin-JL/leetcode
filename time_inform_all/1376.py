#DFS
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = collections.defaultdict(list)
        self.res = 0
        for i, v in enumerate(manager):
            subordinates[v].append(i)
        
        def dfs(manager, time):
            self.res = max(self.res, time)
            for subordinate in subordinates[manager]:
                dfs(subordinate, time + informTime[manager])
        dfs(headID, 0)        
        return self.res

#BFS
class Solution2:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        q = collections.deque([(headID, 0)])
        subordinates = collections.defaultdict(list)
        res = 0
        for i, v in enumerate(manager):
            subordinates[v].append(i)
            
        while q:
            u, time = q.popleft()
            res = max(res, time)
            for v in subordinates[u]:
                q.append((v, time + informTime[u]))
        return res