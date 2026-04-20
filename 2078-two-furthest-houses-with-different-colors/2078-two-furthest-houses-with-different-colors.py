from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)

        # distance from left (0) to farthest different color
        d1 = 0
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:
                d1 = i
                break

        # distance from right (n-1) to farthest different color
        d2 = 0
        for i in range(n):
            if colors[i] != colors[n - 1]:
                d2 = (n - 1) - i
                break

        return max(d1, d2)