class Solution {
    public int[][] constructProductMatrix(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        int mod = 12345;
        int size = n * m;

        int[] arr = new int[size];
        
        int idx = 0;
        for (int[] row : grid) {
            for (int val : row) {
                arr[idx++] = val % mod;
            }
        }

        int[] resultArr = new int[size];

        resultArr[0] = 1;
        for (int i = 1; i < size; i++) {
            resultArr[i] = (resultArr[i - 1] * arr[i - 1]) % mod;
        }

        int suffix = 1;
        for (int i = size - 1; i >= 0; i--) {
            resultArr[i] = (resultArr[i] * suffix) % mod;
            suffix = (suffix * arr[i]) % mod;
        }

        int[][] res = new int[n][m];
        idx = 0;
        for (int i = 0; i < size; i++) {
            res[idx / m][idx % m] = resultArr[i];
            idx++;
        }

        return res;
    }
}