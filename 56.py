from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Sort intervals by ascending start
        intervals.sort(key=lambda x: x[0])

        merged = []
        cur_start, cur_end = intervals[0]

        for start, end in intervals[1:]:
            if start <= cur_end:
                # Overlapping -> extend current interval's end
                cur_end = max(cur_end, end)
            else:
                # Disjoint -> finalize the previous and start a new one
                merged.append([cur_start, cur_end])
                cur_start, cur_end = start, end

        # Append the very last interval
        merged.append([cur_start, cur_end])
        return merged
