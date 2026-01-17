class Solution {
    public long largestSquareArea(int[][] bottomLeft, int[][] topRight) {
        int n = bottomLeft.length;
        long maxArea = 0;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {

                int xLeft   = Math.max(bottomLeft[i][0], bottomLeft[j][0]);
                int yBottom = Math.max(bottomLeft[i][1], bottomLeft[j][1]);
                int xRight  = Math.min(topRight[i][0], topRight[j][0]);
                int yTop    = Math.min(topRight[i][1], topRight[j][1]);

                int width  = xRight - xLeft;
                int height = yTop - yBottom;

                if (width > 0 && height > 0) {
                    long side = Math.min(width, height);
                    maxArea = Math.max(maxArea, side * side);
                }
            }
        }
        return maxArea;
    }
}