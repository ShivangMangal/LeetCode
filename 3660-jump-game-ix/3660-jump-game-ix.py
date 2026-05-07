from typing import List
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n
        pref[0] = nums[0]
        for i in range(1, n):
            pref[i] = max(pref[i - 1], nums[i])
        suff = [0] * n
        suff[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suff[i] = min(suff[i + 1], nums[i])
        ans = [0] * n
        start = 0
        for i in range(n - 1):
            if pref[i] <= suff[i + 1]:
                mx = max(nums[start:i + 1])
                for j in range(start, i + 1):
                    ans[j] = mx
                start = i + 1
        mx = max(nums[start:])
        for j in range(start, n):
            ans[j] = mx
        return ans