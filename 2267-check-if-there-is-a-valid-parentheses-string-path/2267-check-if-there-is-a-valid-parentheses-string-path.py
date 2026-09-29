class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        if (m + n - 1) % 2 == 1:
            return False

        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]

        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):

                for depth in dp[i][j]:

                    if i + 1 < m:
                        if grid[i + 1][j] == '(':
                            new_depth = depth + 1
                        else:
                            new_depth = depth - 1

                        if new_depth >= 0:
                            dp[i + 1][j].add(new_depth)

                    if j + 1 < n:
                        if grid[i][j + 1] == '(':
                            new_depth = depth + 1
                        else:
                            new_depth = depth - 1

                        if new_depth >= 0:
                            dp[i][j + 1].add(new_depth)

        return 0 in dp[m - 1][n - 1]