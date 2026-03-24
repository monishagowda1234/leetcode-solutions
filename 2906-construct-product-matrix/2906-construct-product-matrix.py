class Solution:
    def constructProductMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        m = len(grid[0])
        MOD = 12345
        
        # Initialize the product matrix p with 1s
        p = [[1] * m for _ in range(n)]
        
        # Step 1: Forward Pass (Prefix Product)
        # Calculate the product of all elements appearing before grid[i][j]
        current_product = 1
        for r in range(n):
            for c in range(m):
                p[r][c] = current_product
                current_product = (current_product * grid[r][c]) % MOD
        
        # Step 2: Backward Pass (Suffix Product)
        # Multiply the existing prefix product by the product of all elements after grid[i][j]
        current_product = 1
        for r in range(n - 1, -1, -1):
            for c in range(m - 1, -1, -1):
                p[r][c] = (p[r][c] * current_product) % MOD
                current_product = (current_product * grid[r][c]) % MOD
                
        return p