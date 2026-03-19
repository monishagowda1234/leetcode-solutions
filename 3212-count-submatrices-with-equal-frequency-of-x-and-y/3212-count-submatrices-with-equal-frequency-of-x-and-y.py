class Solution:
    def numberOfSubmatrices(self, grid):
        m, n = len(grid), len(grid[0])
        
        # Convert grid to numbers
        val = [[0]*n for _ in range(m)]
        hasX = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'X':
                    val[i][j] = 1
                    hasX[i][j] = 1
                elif grid[i][j] == 'Y':
                    val[i][j] = -1
        
        # Prefix sums
        ps = [[0]*(n+1) for _ in range(m+1)]
        px = [[0]*(n+1) for _ in range(m+1)]  # count of X
        
        for i in range(m):
            for j in range(n):
                ps[i+1][j+1] = val[i][j] + ps[i][j+1] + ps[i+1][j] - ps[i][j]
                px[i+1][j+1] = hasX[i][j] + px[i][j+1] + px[i+1][j] - px[i][j]
        
        res = 0
        
        # Check all submatrices from (0,0) to (i,j)
        for i in range(m):
            for j in range(n):
                total = ps[i+1][j+1]
                x_count = px[i+1][j+1]
                
                if total == 0 and x_count > 0:
                    res += 1
        
        return res