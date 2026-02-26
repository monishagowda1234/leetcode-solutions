class Solution {
    public int maxSideLength(int[][] mat, int threshold) {
        int m = mat.length;
        int n = mat[0].length;
        int[][] prefixSum = new int[m + 1][n + 1];

        // 1. Build the 2D prefix sum array
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                prefixSum[i][j] = mat[i - 1][j - 1] 
                                + prefixSum[i - 1][j] 
                                + prefixSum[i][j - 1] 
                                - prefixSum[i - 1][j - 1];
            }
        }

        int maxSide = 0;
        
        // 2. Iterate through the matrix and try to expand the square size
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                // We only care if we can find a square bigger than our current best
                int nextSide = maxSide + 1;
                
                // Check if a square of side 'nextSide' ending at (i, j) is within bounds
                if (i >= nextSide && j >= nextSide) {
                    int currentSum = prefixSum[i][j] 
                                   - prefixSum[i - nextSide][j] 
                                   - prefixSum[i][j - nextSide] 
                                   + prefixSum[i - nextSide][j - nextSide];
                    
                    if (currentSum <= threshold) {
                        maxSide = nextSide;
                    }
                }
            }
        }

        return maxSide;
    }
}