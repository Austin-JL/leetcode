import collections

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for a,b in connections:
            graph[a].append((b,1))
            graph[b].append((a,-1))
        
        
        self.ans = 0
        self.visited = set()
        
        def dfs(city):
            self.visited.add(city)
            for edge,road in graph[city]:
                if edge in self.visited:
                    continue
                if road == 1:
                    self.ans += 1
                dfs(edge)
        dfs(0)
        return self.ans


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for a,b in connections:
            graph[a].append((b,1))
            graph[b].append((a,-1))
         
        ans = 0
        dq = collections.deque()
        dq.append(0)
        visited = set()
        
        while dq:
            city = dq.popleft()
            visited.add(city)
            for edge,path in graph[city]:
                if edge not in visited:
                    dq.append(edge)
                    if path == 1:
                        ans += 1
        return ans