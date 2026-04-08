class Solution:
    def xorAfterQueries(self, nums, queries):
        MOD = 10**9 + 7
        
        # Process each query
        for li, ri, ki, vi in queries:
            idx = li
            while idx <= ri:
                nums[idx] = (nums[idx] * vi) % MOD
                idx += ki
        
        # Compute XOR of all elements
        result = 0
        for num in nums:
            result ^= num
        
        return result