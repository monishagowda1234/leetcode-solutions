class Solution:
    def closestTarget(self, words, target, startIndex):
        n = len(words)
        ans = float('inf')
        
        for i in range(n):
            if words[i] == target:
                diff = abs(i - startIndex)
                distance = min(diff, n - diff)
                ans = min(ans, distance)
        
        return ans if ans != float('inf') else -1