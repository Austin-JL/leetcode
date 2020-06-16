class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
        # using floyd warshall
        dp = [[float("inf") for _ in range(N)] for _ in range(N)]
        for u, v, w in times:
            dp[u-1][v-1] = w
        for i in range(N):
            dp[i][i] = 0
            
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    dp[i][j] = min(dp[i][j],dp[i][k]+dp[k][j])
        ans = max(dp[K-1])
        return ans if ans < float("inf") else -1

# using spfa
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
        # using bfs
        graph = collections.defaultdict(list)
        for u,v,w in times:
            graph.setdefault(u,[]).append((v,w))
            
        dq = collections.deque()
        dq.append((0,K))
        ans = [0] + [float("inf")] * N
        while dq:
            time,node = dq.popleft()
            if time < ans[node]:
                ans[node] = time
                for v,w in graph[node]:
                    dq.append((time+w,v))
        time = max(ans)
        return time if time < float("inf") else -1