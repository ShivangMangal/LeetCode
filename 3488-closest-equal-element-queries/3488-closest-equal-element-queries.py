from collections import defaultdict
import bisect
from typing import List
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        pos = defaultdict(list)
        for i, val in enumerate(nums):
            pos[val].append(i)
        res = []
        for q in queries:
            val = nums[q]
            indices = pos[val]
            if len(indices) == 1:
                res.append(-1)
                continue
            idx = bisect.bisect_left(indices, q)
            if indices[idx] == q:
                right = indices[(idx + 1) % len(indices)]
                left = indices[(idx - 1) % len(indices)]
            else:
                right = indices[idx % len(indices)]
                left = indices[(idx - 1) % len(indices)]
            ans = float('inf')
            for j in (left, right):
                d = abs(q - j)
                ans = min(ans, d, n - d)
            res.append(ans)
        return res