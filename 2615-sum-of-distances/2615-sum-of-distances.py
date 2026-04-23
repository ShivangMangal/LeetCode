from typing import List
from collections import defaultdict
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        index_map = defaultdict(list)
        for i, num in enumerate(nums):
            index_map[num].append(i)
        res = [0] * len(nums)
        for indices in index_map.values():
            n = len(indices)
            prefix = [0] * (n + 1)
            for i in range(n):
                prefix[i + 1] = prefix[i] + indices[i]
            for i in range(n):
                pos = indices[i]
                left = pos * i - prefix[i]
                right = (prefix[n] - prefix[i + 1]) - pos * (n - i - 1)
                res[pos] = left + right
        return res