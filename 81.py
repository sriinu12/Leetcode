from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        Returns True if target exists in rotated sorted array nums
        that may contain duplicates; otherwise False.
        Time: O(log n) average, O(n) worst-case. Space: O(1).
        """
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Found target
            if nums[mid] == target:
                return True
            
            # If duplicates at both ends, shrink inward
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
            
            # Left half is sorted
            elif nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return False
    
# Key Features
# Handles Rotated Arrays:
# The algorithm identifies which half of the array is sorted and narrows the search accordingly.
# Handles Duplicates:
# When duplicates obscure the sorted order, the search range is adjusted by shrinking both ends.
# Time Complexity:
# Average Case: O(log n) (binary search).
# Worst Case: O(n) (when duplicates force linear search).
# Space Complexity:
# O(1) (no additional space is used).
