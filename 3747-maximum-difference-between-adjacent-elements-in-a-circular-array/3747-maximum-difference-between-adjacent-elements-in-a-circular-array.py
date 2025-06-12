class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        # Start with the wrap-around pair
        max_diff = abs(nums[0] - nums[-1])
        
        # Check all other adjacent pairs
        for i in range(1, n):
            diff = abs(nums[i] - nums[i - 1])
            if diff > max_diff:
                max_diff = diff
        
        return max_diff
        