class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setChar = set()
        l = 0
        sol = 0

        for r in range(len(s)):
            while s[r] in setChar:
                setChar.remove(s[l])
                l += 1
            setChar.add(s[r])
            sol = max(sol, r - l + 1)
        return sol