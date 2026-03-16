class Solution:
    def getBiggestThree(self, grid):
        m, n = len(grid), len(grid[0])
        res = set()

        for i in range(m):
            for j in range(n):
                # area 0 rhombus (single cell)
                res.add(grid[i][j])

                k = 1
                while True:
                    if i-k < 0 or i+k >= m or j-k < 0 or j+k >= n:
                        break

                    s = 0

                    # 4 edges of rhombus
                    for t in range(k):
                        s += grid[i-k+t][j+t]      # top-right
                        s += grid[i+t][j+k-t]      # right-bottom
                        s += grid[i+k-t][j-t]      # bottom-left
                        s += grid[i-t][j-k+t]      # left-top

                    res.add(s)
                    k += 1

        ans = sorted(res, reverse=True)
        return ans[:3]