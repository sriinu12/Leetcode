class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = ans = nums[0]
        for x in nums[1:]:
            if x < 0:
                max_prod, min_prod = min_prod, max_prod
            max_prod = max(x, max_prod * x)
            min_prod = min(x, min_prod * x)
            ans = max(ans, max_prod)
        return ans
        