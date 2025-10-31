class Solution {
    public int[] getSneakyNumbers(int[] nums) {
        int n = nums.length - 2; 
        int[] count = new int[n];
        int[] result = new int[2];
        int idx = 0;
        for (int num : nums) {
            count[num]++;
            if (count[num] == 2) {
                result[idx++] = num;
            }
        }
        return result;
    }
}