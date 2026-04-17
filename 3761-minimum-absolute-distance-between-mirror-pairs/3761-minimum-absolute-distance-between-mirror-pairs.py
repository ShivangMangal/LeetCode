from typing import List
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse_num(x: int) -> int:
            return int(str(x)[::-1])
        seen = {}  
        min_dist = float('inf')
        for j in range(len(nums)):
            if nums[j] in seen:
                min_dist = min(min_dist, j - seen[nums[j]])
            seen[reverse_num(nums[j])] = j
        return min_dist if min_dist != float('inf') else -1