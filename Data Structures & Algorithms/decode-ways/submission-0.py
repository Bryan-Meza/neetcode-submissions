class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]

            if start == len(s):
                return 1

            ways = 0
            # Value not left zero
            if s[start] == '0':
                return ways
            # Check one char
            ways += dfs(start + 1)
            if 10 <= int(s[start:start + 2]) <= 26:
                ways += dfs(start + 2)

            memo[start] = ways

            return ways

        return dfs(0)