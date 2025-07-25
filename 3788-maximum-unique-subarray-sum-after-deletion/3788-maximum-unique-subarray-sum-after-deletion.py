class Solution:
    def maxSum(self, nums: List[int]) -> int:
        # Find the single largest element
        max_val = max(nums)
        if max_val <= 0:
            return max_val
        
        # Sum all distinct positives
        return sum(x for x in set(nums) if x > 0)
        