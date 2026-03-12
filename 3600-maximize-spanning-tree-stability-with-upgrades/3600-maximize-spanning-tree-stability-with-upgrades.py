class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:

        def can(x):
            dsu = DSU(n)
            upgrades = 0
            used = 0

            # first include mandatory edges
            for u, v, s, must in edges:
                if must:
                    if s < x:
                        return False
                    if not dsu.union(u, v):
                        return False
                    used += 1

            # optional edges
            normal = []
            upgrade = []

            for u, v, s, must in edges:
                if must:
                    continue
                if s >= x:
                    normal.append((u, v))
                elif 2*s >= x:
                    upgrade.append((u, v))

            for u, v in normal:
                if dsu.union(u, v):
                    used += 1

            for u, v in upgrade:
                if used == n-1:
                    break
                if upgrades == k:
                    break
                if dsu.union(u, v):
                    upgrades += 1
                    used += 1

            return used == n-1

        left, right = 1, 2*10**5
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans