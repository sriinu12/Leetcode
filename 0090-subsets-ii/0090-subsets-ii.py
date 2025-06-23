class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()                   # 1. Sort to bring duplicates together
        res: List[List[int]] = []
        subset: List[int] = []

        def backtrack(start: int):
            # Add a copy of current subset
            res.append(subset.copy())

            # Try to include nums[j] for j in [start..len(nums))
            for j in range(start, len(nums)):
                # Skip duplicates: if same as previous at this level, skip
                if j > start and nums[j] == nums[j - 1]:
                    continue

                # Include nums[j]
                subset.append(nums[j])
                backtrack(j + 1)
                # Backtrack: remove last element
                subset.pop()

        backtrack(0)
        return res
        