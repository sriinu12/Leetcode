class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                # Swap current 0 into the 'low' region
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # 1 is in the correct middle region
                mid += 1
            else:
                # Swap current 2 into the 'high' region
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        """
        Do not return anything, modify nums in-place instead.
        """
    
        