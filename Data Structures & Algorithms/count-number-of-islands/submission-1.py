class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = [[False] * cols for _ in range(rows)]

        count = 0 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and not seen[r][c]:
                    count += 1

                    stack = [(r, c)]

                    seen[r][c] = True

                    while stack:
                        x, y = stack.pop()

                        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            nx, ny = x + dx, y + dy

                            if (0 <= nx < rows and 0 <= ny < cols 
                                    and grid[nx][ny] == '1'
                                    and not seen[nx][ny]):
                                seen[nx][ny] = True
                                stack.append((nx, ny))

        return count
