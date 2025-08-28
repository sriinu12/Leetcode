class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diag = collections.defaultdict(list)

        # 1) collect values by diagonal key (i - j)
        for i in range(n):
            for j in range(n):
                diag[i - j].append(grid[i][j])

        # 2) sort: upper diagonals (key < 0) descending, else ascending
        for k in diag:
            diag[k].sort(reverse=(k < 0))

        # 3) rebuild result by popping from the end (O(1) amortized)
        ans = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                k = i - j
                ans[i][j] = diag[k].pop()  # matches the required direction

        return ans
        