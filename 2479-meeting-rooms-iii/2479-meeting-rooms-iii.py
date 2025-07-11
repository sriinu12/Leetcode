class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # 1) Sort by original start time
        meetings.sort(key=lambda x: x[0])
        
        # 2) Min-heaps for idle rooms and busy rooms
        idle = list(range(n))
        heapq.heapify(idle)
        # busy holds (freeTime, roomId)
        busy: List[tuple[int,int]] = []
        
        # 3) Count how many meetings each room hosts
        count = [0] * n
        
        for s, e in meetings:
            # free up rooms that have become available by time s
            while busy and busy[0][0] <= s:
                freeTime, room = heapq.heappop(busy)
                heapq.heappush(idle, room)
            
            dur = e - s
            
            if idle:
                # assign to the smallest-numbered free room
                room = heapq.heappop(idle)
                count[room] += 1
                # schedule at [s, e)
                heapq.heappush(busy, (e, room))
            else:
                # no free room → delay until the earliest one frees up
                freeTime, room = heapq.heappop(busy)
                count[room] += 1
                # delay meeting by shifting to [freeTime, freeTime+dur)
                heapq.heappush(busy, (freeTime + dur, room))
        
        # 4) Return the room with the max count (tie → lowest index)
        return max(range(n), key=lambda i: (count[i], -i))
        