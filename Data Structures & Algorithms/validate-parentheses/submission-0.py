class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if ans and ans[-1] == closeToOpen[c]:
                    ans.pop()
                else:
                    return False
            else:
                ans.append(c)
        return not ans
        