class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        nums.sort()
        return nums == list(range(1, n + 1)) + [n]