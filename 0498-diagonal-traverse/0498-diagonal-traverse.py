class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        diags = [[] for _ in range(m + n - 1)]
        for r in range(m):
            for c in range(n):
                diags[r + c].append(mat[r][c])
        res = []
        for i, arr in enumerate(diags):
            res.extend(arr[::-1] if i % 2 == 0 else arr)
        return res
        