class Solution {
    public int maxProductPath(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        
        long[][] maxDP = new long[m][n];
        long[][] minDP = new long[m][n];
        
        maxDP[0][0] = grid[0][0];
        minDP[0][0] = grid[0][0];
        
        for (int i = 1; i < m; i++) {
            maxDP[i][0] = maxDP[i-1][0] * grid[i][0];
            minDP[i][0] = minDP[i-1][0] * grid[i][0];
        }
        
        for (int j = 1; j < n; j++) {
            maxDP[0][j] = maxDP[0][j-1] * grid[0][j];
            minDP[0][j] = minDP[0][j-1] * grid[0][j];
        }
        
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                long val = grid[i][j];
                
                long a = val * maxDP[i-1][j];
                long b = val * minDP[i-1][j];
                long c = val * maxDP[i][j-1];
                long d = val * minDP[i][j-1];
                
                maxDP[i][j] = Math.max(Math.max(a, b), Math.max(c, d));
                minDP[i][j] = Math.min(Math.min(a, b), Math.min(c, d));
            }
        }
        
        long res = maxDP[m-1][n-1];
        int MOD = 1_000_000_007;
        
        if (res < 0) return -1;
        return (int)(res % MOD);
    }
}