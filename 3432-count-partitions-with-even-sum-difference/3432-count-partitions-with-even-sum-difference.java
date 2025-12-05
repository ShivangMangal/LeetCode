class Solution {
    public int countPartitions(int[] nums) {
        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }
        if (totalSum % 2 != 0) return 0;
        return nums.length - 1;
    }
}
