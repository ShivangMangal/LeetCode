from typing import List
from bisect import bisect_right
class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1
        cntDiv = [0] * (mx + 1)
        for g in range(1, mx + 1):
            for multiple in range(g, mx + 1, g):
                cntDiv[g] += freq[multiple]
        exact = [0] * (mx + 1)
        for g in range(mx, 0, -1):
            c = cntDiv[g]
            pairs = c * (c - 1) // 2
            multiple = g * 2
            while multiple <= mx:
                pairs -= exact[multiple]
                multiple += g
            exact[g] = pairs
        prefix = [0] * (mx + 1)
        for g in range(1, mx + 1):
            prefix[g] = prefix[g - 1] + exact[g]
        ans = []
        for q in queries:
            ans.append(bisect_right(prefix, q))
        return ans