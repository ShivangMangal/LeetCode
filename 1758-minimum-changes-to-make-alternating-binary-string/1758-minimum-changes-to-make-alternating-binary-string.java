class Solution {
    public int minOperations(String s) {
        int count1 = 0; 
        int count2 = 0; 

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (i % 2 == 0) {
                if (c != '0') count1++;
                if (c != '1') count2++;
            } else {
                if (c != '1') count1++;
                if (c != '0') count2++;
            }
        }
        return Math.min(count1, count2);
    }
}