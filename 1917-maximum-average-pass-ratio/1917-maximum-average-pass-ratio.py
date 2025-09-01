class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(p: int, t: int) -> float:
            # Exact algebraic form of the improvement
            return (t - p) / (t * (t + 1))

        # Max-heap using negative gain
        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        k = extraStudents
        while k > 0:
            g, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            heapq.heappush(heap, (-gain(p, t), p, t))
            k -= 1

        # Compute the final average
        total = 0.0
        for _, p, t in heap:
            total += p / t
        return total / len(heap)
        