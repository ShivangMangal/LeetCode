class Solution {
    public String largestGoodInteger(String num) {
        int maxDigit = -1;

        for (int i = 0; i <= num.length() - 3; i++) {
            char a = num.charAt(i);
            char b = num.charAt(i + 1);
            char c = num.charAt(i + 2);

            if (a == b && b == c) {
                int digit = a - '0';
                maxDigit = Math.max(maxDigit, digit);
            }
        }

        if (maxDigit == -1) {
            return "";
        }

        return "" + maxDigit + maxDigit + maxDigit;
    }
}