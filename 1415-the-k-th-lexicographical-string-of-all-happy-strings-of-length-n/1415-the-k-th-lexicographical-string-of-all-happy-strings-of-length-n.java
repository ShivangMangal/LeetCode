class Solution {

    int count = 0;
    String result = "";

    public String getHappyString(int n, int k) {
        dfs("", n, k);
        return result;
    }

    private void dfs(String curr, int n, int k) {
        if (curr.length() == n) {
            count++;
            if (count == k) {
                result = curr;
            }
            return;
        }

        for (char ch : new char[]{'a','b','c'}) {
            if (curr.length() > 0 && curr.charAt(curr.length() - 1) == ch) {
                continue;
            }

            if (!result.isEmpty()) return; 

            dfs(curr + ch, n, k);
        }
    }
}