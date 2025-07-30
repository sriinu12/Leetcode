class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # 1. Find the maximum value in nums
        mx = max(nums)
        
        # 2. Track current run length and best answer
        ans = cur = 0
        for v in nums:
            if v == mx:
                cur += 1
                if cur > ans:
                    ans = cur
            else:
                cur = 0
        
        # 3. Return the longest run
        return ans
        