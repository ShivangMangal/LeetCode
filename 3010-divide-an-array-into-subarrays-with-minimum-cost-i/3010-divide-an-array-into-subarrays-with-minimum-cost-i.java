class Solution {
    public int minimumCost(int[] nums) {
        int n = nums.length;
        int minSum = Integer.MAX_VALUE;
        for (int i = 1; i <= n - 2; i++) {
            for (int j = i + 1; j <= n - 1; j++) {
                minSum = Math.min(minSum, nums[i] + nums[j]);
            }
        }

        return nums[0] + minSum;
    }
}
