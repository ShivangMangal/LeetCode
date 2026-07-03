from typing import List
from collections import deque
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        max_cost = 0
        for u, v, c in edges:
            adj[u].append((v, c))
            indegree[v] += 1
            if c > max_cost:
                max_cost = c
        q = deque(i for i in range(n) if indegree[i] == 0)
        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        INF = 10**30
        def check(threshold: int) -> bool:
            dist = [INF] * n
            dist[0] = 0
            for u in topo:
                if u != 0 and u != n - 1 and not online[u]:
                    continue
                if dist[u] == INF:
                    continue
                for v, c in adj[u]:
                    if c < threshold:
                        continue
                    if v != 0 and v != n - 1 and not online[v]:
                        continue
                    nd = dist[u] + c
                    if nd < dist[v]:
                        dist[v] = nd
            return dist[n - 1] <= k
        if not check(0):
            return -1
        lo, hi = 0, max_cost
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans