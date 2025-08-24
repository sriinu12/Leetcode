from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeros = 0
        best = 0

        for right, v in enumerate(nums):
            if v == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            # window [left..right] has <= 1 zero; delete one element → length = (right-left)
            best = max(best, right - left)

        return best
