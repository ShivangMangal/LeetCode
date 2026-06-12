from typing import List
from collections import deque
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(edges) + 1
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        LOG = (n).bit_length()
        depth = [0] * (n + 1)
        up = [[0] * LOG for _ in range(n + 1)]
        q = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True
        while q:
            u = q.popleft()
            for v in g[u]:
                if not visited[v]:
                    visited[v] = True
                    depth[v] = depth[u] + 1
                    up[v][0] = u
                    for j in range(1, LOG):
                        up[v][j] = up[up[v][j - 1]][j - 1]
                    q.append(v)
        def lca(a: int, b: int) -> int:
            if depth[a] < depth[b]:
                a, b = b, a
            diff = depth[a] - depth[b]
            for j in range(LOG):
                if diff & (1 << j):
                    a = up[a][j]
            if a == b:
                return a
            for j in range(LOG - 1, -1, -1):
                if up[a][j] != up[b][j]:
                    a = up[a][j]
                    b = up[b][j]
            return up[a][0]
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % MOD
        ans = []
        for u, v in queries:
            w = lca(u, v)
            k = depth[u] + depth[v] - 2 * depth[w]
            if k == 0:
                ans.append(0)
            else:
                ans.append(pow2[k - 1])
        return ans