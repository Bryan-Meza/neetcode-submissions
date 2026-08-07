class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        if not digits:
            return []

        res = []

        def dfs(start, path):
            if start == len(digits):
                res.append(''.join(path))
                return

            next_number = digits[start]
            for letter in keyboard[next_number]:
                path.append(letter)
                dfs(start + 1, path)
                path.pop()


        dfs(0, [])
        
        return res