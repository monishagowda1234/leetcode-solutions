import java.util.*;

class Solution {
    public int minCost(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;
        long INF = Long.MAX_VALUE / 2;
        
        // dp[i][j] stores the min cost to reach (i, j) with current number of teleports
        long[][] dp = new long[m][n];
        for (long[] row : dp) Arrays.fill(row, INF);
        
        // Starting position cost is 0 (as per the destination-based cost rule)
        dp[0][0] = 0;
        long minTotalCost = INF;

        for (int u = 0; u <= k; u++) {
            // 1. Calculate Normal Moves (Right and Down) for the current 'u' teleports
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (i > 0) dp[i][j] = Math.min(dp[i][j], dp[i - 1][j] + grid[i][j]);
                    if (j > 0) dp[i][j] = Math.min(dp[i][j], dp[i][j - 1] + grid[i][j]);
                }
            }

            // Update the global answer with the cost to reach the bottom-right
            minTotalCost = Math.min(minTotalCost, dp[m - 1][n - 1]);

            // 2. Prepare for the next teleport (u+1)
            if (u < k) {
                long[][] nextDp = new long[m][n];
                for (long[] row : nextDp) Arrays.fill(row, INF);

                // Find the minimum cost reached so far for each grid value
                long[] minAtVal = new long[10001];
                Arrays.fill(minAtVal, INF);
                for (int i = 0; i < m; i++) {
                    for (int j = 0; j < n; j++) {
                        minAtVal[grid[i][j]] = Math.min(minAtVal[grid[i][j]], dp[i][j]);
                    }
                }

                // Suffix minimum: best cost from any cell with value >= V
                long suffixMin = INF;
                long[] bestToTeleportTo = new long[10001];
                for (int v = 10000; v >= 0; v--) {
                    suffixMin = Math.min(suffixMin, minAtVal[v]);
                    bestToTeleportTo[v] = suffixMin;
                }

                // Initialize nextDp: Either teleport to (i, j) or stay with current cost
                for (int i = 0; i < m; i++) {
                    for (int j = 0; j < n; j++) {
                        // Cost to teleport to (i, j) is the best cost from any cell with grid[x][y] >= grid[i][j]
                        long teleportCost = bestToTeleportTo[grid[i][j]];
                        nextDp[i][j] = Math.min(dp[i][j], teleportCost);
                    }
                }
                dp = nextDp;
            }
        }

        return (int) minTotalCost;
    }
}