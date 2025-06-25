class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res: List[List[int]] = []
        combo: List[int] = []

        def backtrack(start: int, remaining: int):
            if remaining == 0:
                res.append(combo.copy())
                return
            # Try each candidate once
            prev = -1  # track last used at this level to skip duplicates
            for i in range(start, len(candidates)):
                curr = candidates[i]
                # Skip duplicates
                if curr == prev:
                    continue
                # If too large, no need to continue (sorted order)
                if curr > remaining:
                    break

                # Choose
                combo.append(curr)
                backtrack(i + 1, remaining - curr)
                combo.pop()

                # Mark this value as used at this level
                prev = curr

        backtrack(0, target)
        return res
        