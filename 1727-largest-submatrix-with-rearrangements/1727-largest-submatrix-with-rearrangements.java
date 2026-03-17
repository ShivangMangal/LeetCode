import java.util.*;

class Solution {
    public int largestSubmatrix(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;

        int[][] height = new int[m][n];

        for (int j = 0; j < n; j++) {
            height[0][j] = matrix[0][j];
        }

        for (int i = 1; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 1) {
                    height[i][j] = height[i - 1][j] + 1;
                } else {
                    height[i][j] = 0;
                }
            }
        }

        int maxArea = 0;

        for (int i = 0; i < m; i++) {
            int[] row = Arrays.copyOf(height[i], n);
            Arrays.sort(row);

            for (int j = 0; j < n; j++) {
                int h = row[n - 1 - j];
                int w = j + 1;
                maxArea = Math.max(maxArea, h * w);
            }
        }

        return maxArea;
    }
}