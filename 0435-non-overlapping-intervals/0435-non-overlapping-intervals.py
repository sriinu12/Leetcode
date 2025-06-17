class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort intervals by their end time
        intervals.sort(key=lambda x: x[1])
        
        removals = 0
        # End time of the last interval we kept
        prev_end = intervals[0][1]
        
        # Iterate through the rest
        for start, end in intervals[1:]:
            if start < prev_end:
                # Overlaps: we must remove this interval
                removals += 1
            else:
                # No overlap: keep it and update prev_end
                prev_end = end
        
        return removals
        