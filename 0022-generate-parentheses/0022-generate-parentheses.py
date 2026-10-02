class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        self.res = []

        def bt(start, curr, d):
            if d < 0: return

            if start == n * 2:
                if d == 0: self.res.append(curr)
                return 

            bt(start+1, curr +'(',d + 1)
            bt(start+1, curr + ')',d - 1)

        bt(0,'',0)
        return self.res
        