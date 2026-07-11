from collections import defaultdict
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = [False] * n
        ans = 0
        def dfs(node):
            visited[node] = True
            nodes = 1
            degreeSum = len(graph[node])
            for nei in graph[node]:
                if not visited[nei]:
                    a, b = dfs(nei)
                    nodes += a
                    degreeSum += b
            return nodes, degreeSum
        for i in range(n):
            if not visited[i]:
                nodes, degreeSum = dfs(i)
                edgeCount = degreeSum // 2

                if edgeCount == nodes * (nodes - 1) // 2:
                    ans += 1
        return ans