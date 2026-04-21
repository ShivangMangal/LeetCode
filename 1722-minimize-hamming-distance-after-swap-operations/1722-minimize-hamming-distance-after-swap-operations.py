from typing import List
from collections import defaultdict, Counter
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        parent = list(range(len(source)))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px
        for a, b in allowedSwaps:
            union(a, b)
        groups = defaultdict(list)
        for i in range(len(source)):
            groups[find(i)].append(i)
        result = 0
        for indices in groups.values():
            count = Counter()
            for i in indices:
                count[source[i]] += 1
            for i in indices:
                if count[target[i]] > 0:
                    count[target[i]] -= 1
                else:
                    result += 1
        return result