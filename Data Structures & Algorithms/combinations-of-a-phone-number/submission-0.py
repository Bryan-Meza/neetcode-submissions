KEYBOARD = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        res = []
        n = len(digits)

        if not digits:
            return []

        def dfs(start_index, path):
            if start_index == n:
                res.append("".join(path))
                return
            
            next_number = digits[start_index]
            for num in KEYBOARD[next_number]:
                path.append(num)
                dfs(start_index + 1, path)
                path.pop()
            
        dfs(0, [])

        return res  