class Solution {
    public int areaOfMaxDiagonal(int[][] dimensions) {
        int maxDiagonalSq = 0;
        int maxArea = 0;
        for (int[] rect : dimensions) {
            int l = rect[0];
            int w = rect[1];

            int diagonalSq = l * l + w * w;
            int area = l * w;

            if (diagonalSq > maxDiagonalSq) {
                maxDiagonalSq = diagonalSq;
                maxArea = area;
            } else if (diagonalSq == maxDiagonalSq) {
                maxArea = Math.max(maxArea, area);
            }
        }
        return maxArea;
    }
}