class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + (1 if nums[i] == target else -1)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                if prefix[j] - prefix[i] > 0:
                    ans += 1
        return ans