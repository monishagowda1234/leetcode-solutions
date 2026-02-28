class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        res = 0

        for curr in range(1, n + 1):
            res <<= curr.bit_length()   # shift left
            res = (res | curr) % MOD    # add current number

        return res