class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # sort to enable two-pointer and skip duplicates
        
        n = len(nums)
        for i in range(n - 2):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two-pointer search for pairs summing to -nums[i]
            target = -nums[i]
            left, right = i + 1, n - 1
            
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    # Found a valid triplet
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers inward
                    left += 1
                    right -= 1
                elif s < target:
                    # Need a larger sum
                    left += 1
                else:
                    # Need a smaller sum
                    right -= 1
        
        return res
        