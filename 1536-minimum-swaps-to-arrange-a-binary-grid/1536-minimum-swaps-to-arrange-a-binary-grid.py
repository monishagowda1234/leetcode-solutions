class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # Count trailing zeros for each row
        arr = []
        for row in grid:
            count = 0
            for i in range(n - 1, -1, -1):
                if row[i] == 0: count += 1
                else: break
            arr.append(count)

        res = 0
        for i in range(n):
            target = n - 1 - i
            found = False
            
            # Find the first row that satisfies the requirement
            for j in range(i, n):
                if arr[j] >= target:
                    res += (j - i)
                    # Move the found row to the current position
                    arr.insert(i, arr.pop(j))
                    found = True
                    break
            
            if not found: return -1
            
        return res