class Solution {
    public int minimumOperations(int[] nums) {
        int ops = 0;
        for (int num : nums) {
            int r = num % 3;
            if (r != 0) {
                ops++;
            }
        }
        return ops;
    }
}
