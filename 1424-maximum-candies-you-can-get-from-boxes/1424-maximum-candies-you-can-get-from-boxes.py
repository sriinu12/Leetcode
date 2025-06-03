class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        
        # Track which boxes we have in our hand
        inHand = [False] * n
        # Track which boxes we have keys for
        haveKey = [False] * n
        # Track which boxes have been opened already
        opened = [False] * n
        
        # Initialize: put all initial boxes in hand
        for b in initialBoxes:
            inHand[b] = True
        
        # Use a queue for boxes that can be opened immediately
        queue = deque()
        
        # Seed the queue with any initial box that is already open
        for b in initialBoxes:
            if status[b] == 1:   # box b is open
                queue.append(b)
        
        total_candies = 0
        
        # Process until no more openable boxes remain
        while queue:
            b = queue.popleft()
            
            # If we've already opened box b, skip it
            if opened[b]:
                continue
            
            # 1) Open box b
            opened[b] = True
            
            # 2) Collect candies in box b
            total_candies += candies[b]
            
            # 3) Acquire all keys found inside b
            for k in keys[b]:
                if not haveKey[k]:
                    haveKey[k] = True
                    # If we already have that box in hand and it isn't opened, we can now open it
                    if inHand[k] and not opened[k]:
                        queue.append(k)
            
            # 4) Acquire all boxes contained in b
            for c in containedBoxes[b]:
                if not inHand[c]:
                    inHand[c] = True
                    # If c is either open or we already have its key, we can open it now
                    if (status[c] == 1 or haveKey[c]) and not opened[c]:
                        queue.append(c)
        
        return total_candies
        