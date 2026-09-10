class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, start):
            if start == len(word):
                return True
            
            if (r < 0 or r >= rows or c < 0 or c >= cols) or board[r][c] != word[start] or board[r][c] == "#":
                return False
            
            board[r][c] = "#"
            
            res = (dfs(r + 1, c, start + 1) or
                    dfs(r - 1, c, start + 1) or
                    dfs(r, c + 1, start + 1) or
                    dfs(r, c - 1, start + 1))

            board[r][c] = word[start]
            return res
            

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False