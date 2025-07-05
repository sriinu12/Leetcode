class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Build a min-heap of the first k elements
        heap = nums[:k]
        heapq.heapify(heap)
        # For each remaining num, if it's bigger than the heap root, replace
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num)
        # The root is the k-th largest
        return heap[0]
        