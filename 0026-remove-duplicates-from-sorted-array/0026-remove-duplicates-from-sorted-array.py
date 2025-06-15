class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Initialize write pointer at first element
        write_idx = 1
        
        # Start reading from the second element
        for read_idx in range(1, len(nums)):
            # Whenever we see a new value, write it at write_idx and advance write_idx
            if nums[read_idx] != nums[read_idx - 1]:
                nums[write_idx] = nums[read_idx]
                write_idx += 1
        
        # write_idx is the length of the unique portion
        return write_idx
        