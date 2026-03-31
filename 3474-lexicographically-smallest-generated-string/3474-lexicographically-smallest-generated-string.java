class Solution {
    public String generateString(String str1, String str2) {
        int n = str1.length(), m = str2.length();
        char[] word = new char[n + m - 1];
        boolean[] locked = new boolean[n + m - 1];

        for (int i = 0; i < word.length; i++) {
            word[i] = '?';
        }

        for (int i = 0; i < n; i++) {
            if (str1.charAt(i) == 'T') {
                for (int j = 0; j < m; j++) {
                    if (word[i + j] == '?' || word[i + j] == str2.charAt(j)) {
                        word[i + j] = str2.charAt(j);
                        locked[i + j] = true;
                    } else {
                        return "";
                    }
                }
            }
        }

        for (int i = 0; i < word.length; i++) {
            if (word[i] == '?') word[i] = 'a';
        }

        for (int i = 0; i < n; i++) {
            if (str1.charAt(i) == 'F') {
                boolean match = true;

                for (int j = 0; j < m; j++) {
                    if (word[i + j] != str2.charAt(j)) {
                        match = false;
                        break;
                    }
                }

                if (match) {
                    boolean fixed = false;

                    for (int j = m - 1; j >= 0; j--) {
                        int idx = i + j;

                        if (locked[idx]) continue;

                        char original = word[idx];

                        for (char c = 'a'; c <= 'z'; c++) {
                            if (c == original) continue;

                            word[idx] = c;

                            boolean stillMatch = true;
                            for (int k = 0; k < m; k++) {
                                if (word[i + k] != str2.charAt(k)) {
                                    stillMatch = false;
                                    break;
                                }
                            }

                            if (!stillMatch) {
                                fixed = true;
                                break;
                            }

                            word[idx] = original;
                        }

                        if (fixed) break;
                    }

                    if (!fixed) return "";
                }
            }
        }

        return new String(word);
    }
}