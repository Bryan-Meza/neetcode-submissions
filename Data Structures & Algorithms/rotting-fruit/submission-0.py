from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        minutes = 0

        directions = [[1,0], [-1,0], [0, 1], [0, -1]]

        queue = deque()
        
        # Count fresh oranges
        fresh = 0

        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))

        # If theres no fresh, no time is needed
        if fresh == 0:
            return 0

        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < num_rows and 0 <= nc < num_cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))

            minutes += 1
        
        if fresh == 0:
            return minutes

        return -1

