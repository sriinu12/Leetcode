class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        visited = [[False]*n for _ in range(m)]
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        d = 0
        r = c = 0
        out = []
        for _ in range(m*n):
            out.append(matrix[r][c])
            visited[r][c] = True
            nr, nc = r + dirs[d][0], c + dirs[d][1]
            if not (0 <= nr < m and 0 <= nc < n and not visited[nr][nc]):
                d = (d + 1) % 4
                nr, nc = r + dirs[d][0], c + dirs[d][1]
            r, c = nr, nc
        return out
        