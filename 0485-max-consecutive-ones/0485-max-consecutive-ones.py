class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        current = 0
        
        for bit in nums:
            if bit == 1:
                current += 1
                # Update max_count if current run is longer
                if current > max_count:
                    max_count = current
            else:
                # Reset current run when we see a 0
                current = 0
        
        return max_count
        