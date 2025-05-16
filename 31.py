from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Rearranges nums into the lexicographically next greater permutation.
        Modifies in-place. If no next permutation exists, rearranges into the lowest order.
        """
        n = len(nums)
        
        # 1) Find the rightmost pivot where nums[i] < nums[i+1]
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 2) If pivot found, find rightmost successor > nums[i], then swap
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # 3) Reverse the suffix starting at i+1
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
# # Explanation:
# Find Pivot: Scan from right to left to find the first index i where nums[i] < nums[i+1]. If none, the entire array is descending.

# Find Successor: If pivot exists, scan from the right again to find the first index j such that nums[j] > nums[i].

# Swap: Swap nums[i] and nums[j].

# Reverse Suffix: Reverse the subarray nums[i+1:] to get the smallest suffix.