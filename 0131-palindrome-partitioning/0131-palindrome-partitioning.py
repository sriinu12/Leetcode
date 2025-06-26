class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        # 1. Build palindrome DP table
        is_pal = [[False] * n for _ in range(n)]
        for end in range(n):
            for start in range(end + 1):
                if s[start] == s[end] and (end - start < 2 or is_pal[start + 1][end - 1]):
                    is_pal[start][end] = True

        res: List[List[str]] = []
        path: List[str] = []

        # 2. Backtracking DFS
        def dfs(start: int):
            if start == n:
                res.append(path.copy())
                return
            for end in range(start, n):
                if is_pal[start][end]:
                    # choose the palindrome s[start:end+1]
                    path.append(s[start:end+1])
                    dfs(end + 1)
                    path.pop()  # backtrack

        dfs(0)
        return res
        