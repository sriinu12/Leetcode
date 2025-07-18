class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        
        # 1) Prefix: min sum of n elements in nums[0..k-1] for k in [n..2n]
        max_heap = []
        sum_left = 0
        prefix_sum = [0] * (3*n + 1)
        
        # Initial n
        for i in range(n):
            sum_left += nums[i]
            heapq.heappush(max_heap, -nums[i])
        prefix_sum[n] = sum_left
        
        # Extend window to size 2n
        for i in range(n, 2*n):
            sum_left += nums[i]
            heapq.heappush(max_heap, -nums[i])
            # Remove the largest to keep only n smallest
            sum_left += heapq.heappop(max_heap)  # pop returns negative
            prefix_sum[i+1] = sum_left
        
        # 2) Suffix: max sum of n elements in nums[k..3n-1] for k in [n..2n]
        min_heap = []
        sum_right = 0
        suffix_sum = [0] * (3*n + 1)
        
        # Initial last n
        for i in range(3*n - 1, 2*n - 1, -1):
            sum_right += nums[i]
            heapq.heappush(min_heap, nums[i])
        suffix_sum[2*n] = sum_right
        
        # Extend window backwards to size 2n
        for i in range(2*n - 1, n - 1, -1):
            sum_right += nums[i]
            heapq.heappush(min_heap, nums[i])
            # Remove the smallest to keep only n largest
            sum_right -= heapq.heappop(min_heap)
            suffix_sum[i] = sum_right
        
        # 3) Compute minimum difference over all split points k
        ans = float('inf')
        for k in range(n, 2*n + 1):
            ans = min(ans, prefix_sum[k] - suffix_sum[k])
        
        return ans
        