import heapq
from typing import List

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        h = []

        for x in workerTimes:
            heapq.heappush(h, (x, x, 1))  

        res = 0

        for _ in range(mountainHeight):
            acc, base, count = heapq.heappop(h)
            res = acc
            heapq.heappush(h, (acc + base * (count + 1), base, count + 1))

        return res