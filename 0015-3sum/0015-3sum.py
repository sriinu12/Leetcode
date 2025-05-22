class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []
        n = len(nums)
        if n < 3:
            return res
        
        nums.sort()  # Sort to enable two-pointer and duplicate skipping
        
        for i in range(n - 2):
            # If the current value is the same as the one before, we’ve already processed it
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            target = -nums[i]
            lo, hi = i + 1, n - 1
            
            while lo < hi:
                s = nums[lo] + nums[hi]
                if s < target:
                    lo += 1
                elif s > target:
                    hi -= 1
                else:
                    # Found a triplet
                    res.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    # Skip duplicate second and third elements
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
        
        return res
        