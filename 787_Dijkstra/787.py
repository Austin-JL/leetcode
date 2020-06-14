class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for city,edge,path in flights:
            graph[city].append((edge,path))
        prior_queue = [ (0, -1, src) ]
        while prior_queue:
            cost, stops, node = heapq.heappop(prior_queue)
            if stops > K:
                continue
            if node == dst:
                return cost
            for edge,path in graph[node]:
                heapq.heappush(prior_queue, (cost+path, stops + 1, edge))
        return -1