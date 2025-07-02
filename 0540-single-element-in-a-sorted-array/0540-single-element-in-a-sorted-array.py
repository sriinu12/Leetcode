class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            # Ensure mid is even for pairing
            if mid % 2 == 1:
                mid -= 1
            
            # If pair is intact, single is to the right
            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            else:
                # Pair broken, single is at or before mid
                high = mid
        
        return nums[low]
        