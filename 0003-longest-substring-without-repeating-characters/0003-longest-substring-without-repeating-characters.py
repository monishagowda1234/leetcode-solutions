class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charSet = set()
        left = 0
        maxLength = 0

        for right in range(len(s)):

            # remove duplicate characters
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            # add current character
            charSet.add(s[right])

            # update maximum length
            maxLength = max(maxLength, right - left + 1)

        return maxLength