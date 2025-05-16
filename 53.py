from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Kadane's algorithm: One pass, O(n) time, O(1) space.
        curr_sum = max subarray sum ending here.
        best = global maximum over all positions.
        """
        best = nums[0]
        curr_sum = 0
        
        for x in nums:
            # Extend or start new subarray here
            curr_sum = max(x, curr_sum + x)
            # Update global max
            best = max(best, curr_sum)
        
        return best
# # Explanation:
# curr_sum tracks the maximum sum of a subarray ending at the current position (we choose either to extend the previous or start fresh at x).

# best records the overall maximum encountered.

# This naturally handles all‐negative arrays (it will pick the largest negative as best).

# Only one pass over nums is needed, and only two integer variables are used—perfectly optimal.

## Time Complexity: O(n) (linear scan).
## Space Complexity: O(1) (no extra space used).