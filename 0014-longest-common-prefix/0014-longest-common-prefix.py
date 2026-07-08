class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        # Compare each character of the first string
        for i in range(len(strs[0])):
            char = strs[0][i]

            # Check this character with all other strings
            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]

        return strs[0]