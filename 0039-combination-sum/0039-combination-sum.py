class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()             # optional, helps prune earlier
        res: List[List[int]] = []
        path: List[int] = []

        def dfs(start: int, curr_sum: int):
            if curr_sum == target:
                res.append(path.copy())
                return
            if curr_sum > target:
                return

            for i in range(start, len(candidates)):
                # choose candidates[i]
                path.append(candidates[i])
                dfs(i, curr_sum + candidates[i])  # i, not i+1, to allow reuse
                path.pop()                        # backtrack

        dfs(0, 0)
        return res
        