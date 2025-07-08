class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # 1) Sort by start day
        events.sort(key=lambda e: e[0])
        starts = [e[0] for e in events]  # for binary search

        @functools.lru_cache(None)
        def dp(i: int, c: int) -> int:
            # Base cases
            if c == 0 or i == len(events):
                return 0

            # Option 1: skip this event
            ans = dp(i + 1, c)

            # Option 2: take this event
            # Find next index j whose start > current end
            _, end, val = events[i]
            j = bisect.bisect_right(starts, end)
            ans = max(ans, val + dp(j, c - 1))

            return ans

        # 2) Kick off with all k attendances allowed
        return dp(0, k)
        