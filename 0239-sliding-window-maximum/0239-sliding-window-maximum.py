class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 0 or k == 0:
            return []
        
        dq = deque()  # will store indices, nums[...] decreasing
        res: List[int] = []
        
        for i, x in enumerate(nums):
            # 1) Remove indices out of this window
            if dq and dq[0] == i - k:
                dq.popleft()
            
            # 2) Maintain decreasing order in deque
            while dq and nums[dq[-1]] < x:
                dq.pop()
            
            # 3) Add current index
            dq.append(i)
            
            # 4) Record result once first window is ready
            if i >= k - 1:
                res.append(nums[dq[0]])
        
        return res
        