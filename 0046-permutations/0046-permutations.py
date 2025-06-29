class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []
        n = len(nums)

        def backtrack(path: List[int], used: List[bool]):
            # If we've chosen n numbers, record the permutation
            if len(path) == n:
                res.append(path.copy())
                return

            for i in range(n):
                if not used[i]:
                    # choose nums[i]
                    used[i] = True
                    path.append(nums[i])

                    backtrack(path, used)

                    # backtrack
                    path.pop()
                    used[i] = False

        backtrack([], [False] * n)
        return res
        