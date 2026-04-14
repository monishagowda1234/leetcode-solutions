class Solution:
    def minimumTotalDistance(self, robot, factory):
        # Step 1: Sort robots and factories
        robot.sort()
        factory.sort()

        n = len(robot)
        m = len(factory)

        # Step 2: Initialize DP table
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        
        # Base case: no robots = 0 distance
        for j in range(m + 1):
            dp[0][j] = 0

        # Step 3: Fill DP
        for j in range(1, m + 1):
            pos, limit = factory[j - 1]

            for i in range(n + 1):
                # Option 1: skip this factory
                dp[i][j] = dp[i][j - 1]

                # Option 2: assign k robots to this factory
                dist = 0
                for k in range(1, min(i, limit) + 1):
                    # Add distance of k-th robot from end
                    dist += abs(robot[i - k] - pos)
                    dp[i][j] = min(dp[i][j], dp[i - k][j - 1] + dist)

        return dp[n][m]