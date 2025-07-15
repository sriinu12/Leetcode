class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        
        # 1) Initialize queue with all rotten oranges at time=0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1
        
        # Directions: up, down, left, right
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        minutes = 0
        
        # 2) BFS
        while q:
            r, c, t = q.popleft()
            minutes = max(minutes, t)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    # Rot this fresh orange
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc, t + 1))
        
        # 3) If any fresh remain, impossible
        return minutes if fresh == 0 else -1
        