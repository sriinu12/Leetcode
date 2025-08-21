from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        w = 1  # next write position for a new unique
        for i in range(1, len(nums)):
            if nums[i] != nums[w - 1]:
                nums[w] = nums[i]
                w += 1
        return w
