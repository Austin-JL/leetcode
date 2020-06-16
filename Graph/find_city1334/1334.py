class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dis = [[float('inf')] * n for _ in range(n)]
        for i, j, w in edges:
            dis[i][j] = dis[j][i] = w
        for i in range(n):
            dis[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
         
        neighbors = Counter()
        for i in range(n):
            for j in range(n):
                if i != j and dis[i][j] <= distanceThreshold:
                    neighbors[i] += 1
        best = 0
        for i in range(n):
            if neighbors[i] <= neighbors[best]:
                best = i
        return best


        