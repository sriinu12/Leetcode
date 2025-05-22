from typing import List
import heapq

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        """
        LeetCode 3362. Zero Array Transformation III
        
        We want to remove as many queries as possible while still being able to
        decrement each nums[i] times over the remaining queries so that nums becomes all zero.
        Greedy: always remove the shortest-covering queries last by applying the necessary queries
        in order of earliest end-time.
        
        Time: O((n + m) log m)
        Space: O(m)
        """
        n, m = len(nums), len(queries)
        # 1) Sort queries by start index ascending
        queries.sort(key=lambda x: x[0])
        
        # available: max-heap of end indices (negated for Python min-heap)
        available = []
        # running: min-heap of end indices for queries we've "kept"/applied
        running = []
        
        qi = 0        # pointer into sorted queries
        applied = 0   # count of applied (kept) queries
        
        # 2) Scan each index i = 0..n-1
        for i in range(n):
            # Add all queries that begin at i into 'available'
            while qi < m and queries[qi][0] == i:
                # push negative of end for max-heap behavior
                heapq.heappush(available, -queries[qi][1])
                qi += 1
            
            # Remove any applied queries that have already ended before i
            while running and running[0] < i:
                heapq.heappop(running)
            
            # Ensure we have at least nums[i] active queries covering i
            while len(running) < nums[i]:
                # If no available query can cover i, impossible
                if not available or -available[0] < i:
                    return -1
                # Pick the available query with the latest end (max end)
                end = -heapq.heappop(available)
                # Apply/keep it
                heapq.heappush(running, end)
                applied += 1
        
        # We can remove all queries we did NOT apply
        return m - applied
