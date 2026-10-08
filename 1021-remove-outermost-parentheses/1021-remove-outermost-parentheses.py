class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        res = []
        l = 0
        for r in range(len(s)) :
            if s[r] == '(' :
                count += 1
            else :
                count -= 1
            if count == 0 :
                res.append(s[l+1 : r]) 
                l = r+1
        return "".join(res)