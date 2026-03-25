class Solution {
    public boolean canPartitionGrid(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        long totalSum = 0;

        // Step 1: Calculate total sum
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                totalSum += grid[i][j];
            }
        }

        // Step 2: If total sum is odd → impossible
        if (totalSum % 2 != 0) return false;

        // Step 3: Try horizontal cut
        long currentSum = 0;
        for (int i = 0; i < m - 1; i++) {
            for (int j = 0; j < n; j++) {
                currentSum += grid[i][j];
            }
            if (currentSum == totalSum - currentSum) {
                return true;
            }
        }

        // Step 4: Try vertical cut
        currentSum = 0;
        for (int j = 0; j < n - 1; j++) {
            for (int i = 0; i < m; i++) {
                currentSum += grid[i][j];
            }
            if (currentSum == totalSum - currentSum) {
                return true;
            }
        }

        return false;
    }
}