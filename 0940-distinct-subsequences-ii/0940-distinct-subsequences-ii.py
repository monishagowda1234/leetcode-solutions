class Solution:
    def distinctSubseqII(self, s: str) -> int:
        frq = {}
        MOD = 10**9+7
        for char in s:
            curr = (1+sum(frq.values()))%MOD
            frq[char] = curr
        return sum(frq.values())%MOD