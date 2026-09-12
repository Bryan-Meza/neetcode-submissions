class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(word):
            return word == word[::-1]

        def dfs(start, path):
            if start == len(s):
                res.append(path)
                return

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if is_palindrome(word):
                    dfs(end, path + [word])    

        
        dfs(0, [])
        
        
        return res