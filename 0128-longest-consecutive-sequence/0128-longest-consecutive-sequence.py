class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        best = 0

        for num in num_set:
            # only start counting at the beginning of a sequence
            if num - 1 not in num_set:
                length = 1
                cur = num + 1
                # count upward until the sequence breaks
                while cur in num_set:
                    length += 1
                    cur += 1
                best = max(best, length)

        return best
        