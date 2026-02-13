import java.util.*;

class Solution {
    public int longestBalanced(String s) {
        int n = s.length();
        int ans = 1;

 
        int count = 1;
        for (int i = 1; i < n; i++) {
            if (s.charAt(i) == s.charAt(i - 1)) {
                count++;
                ans = Math.max(ans, count);
            } else {
                count = 1;
            }
        }

        ans = Math.max(ans, threeEqual(s));


        ans = Math.max(ans, twoEqual(s, 'a', 'b'));
        ans = Math.max(ans, twoEqual(s, 'a', 'c'));
        ans = Math.max(ans, twoEqual(s, 'b', 'c'));

        return ans;
    }

    private int threeEqual(String s) {
        Map<Long, Integer> map = new HashMap<>();
        int a = 0, b = 0, c = 0;
        int max = 0;

        map.put(0L, -1);

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            if (ch == 'a') a++;
            else if (ch == 'b') b++;
            else c++;

            int d1 = a - b;
            int d2 = a - c;

            long key = (((long)d1) << 32) | (d2 & 0xffffffffL);

            if (map.containsKey(key)) {
                max = Math.max(max, i - map.get(key));
            } else {
                map.put(key, i);
            }
        }

        return max;
    }

    private int twoEqual(String s, char x, char y) {
        int max = 0;
        int start = 0;

        while (start < s.length()) {
            while (start < s.length() &&
                  s.charAt(start) != x &&
                  s.charAt(start) != y) {
                start++;
            }

            if (start >= s.length()) break;

            Map<Integer, Integer> map = new HashMap<>();
            map.put(0, start - 1);

            int diff = 0;
            int i = start;

            while (i < s.length() &&
                  (s.charAt(i) == x || s.charAt(i) == y)) {

                if (s.charAt(i) == x) diff++;
                else diff--;

                if (map.containsKey(diff)) {
                    max = Math.max(max, i - map.get(diff));
                } else {
                    map.put(diff, i);
                }

                i++;
            }

            start = i;
        }

        return max;
    }
}
