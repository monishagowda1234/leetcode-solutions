class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        pre = strs[0]
        for i in strs[1:]:
            while not i.startswith(pre):
                pre = pre[:-1]
        return pre