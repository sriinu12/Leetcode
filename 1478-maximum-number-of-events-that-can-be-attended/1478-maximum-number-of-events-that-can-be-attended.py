class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # 1) Sort events by start day
        events.sort(key=lambda e: e[0])
        
        total_attended = 0
        min_heap = []   # will hold the end days of currently available events
        day = 0
        i = 0
        n = len(events)
        
        # 2) While there are events left or pending in the heap
        while i < n or min_heap:
            # If no available events today, jump forward to the next event's start
            if not min_heap:
                day = events[i][0]
            
            # 3) Add all events that start ≤ current day
            while i < n and events[i][0] <= day:
                heapq.heappush(min_heap, events[i][1])
                i += 1
            
            # 4) Remove expired events (those with end < day)
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
            
            # 5) Attend the event that ends soonest (if any)
            if min_heap:
                heapq.heappop(min_heap)
                total_attended += 1
                day += 1  # move to the next day
        
        return total_attended
        