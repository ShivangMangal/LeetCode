class Solution {
    public int minFlips(String s) {
        int n = s.length();
        String s2 = s + s;

        int alt1 = 0, alt2 = 0;
        int res = Integer.MAX_VALUE;
        int left = 0;

        for (int right = 0; right < s2.length(); right++) {

            char c = s2.charAt(right);

            if (c != (right % 2 == 0 ? '0' : '1')) alt1++;
            if (c != (right % 2 == 0 ? '1' : '0')) alt2++;

            if (right - left + 1 > n) {
                char lc = s2.charAt(left);

                if (lc != (left % 2 == 0 ? '0' : '1')) alt1--;
                if (lc != (left % 2 == 0 ? '1' : '0')) alt2--;

                left++;
            }

            if (right - left + 1 == n) {
                res = Math.min(res, Math.min(alt1, alt2));
            }
        }

        return res;
    }
}