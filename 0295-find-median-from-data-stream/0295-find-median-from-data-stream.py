class MedianFinder:

    def __init__(self):
        # small: max-heap (store negatives)
        # large: min-heap
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        # 1) Add to max-heap (small) as negative
        heapq.heappush(self.small, -num)
        # 2) Balance: move the largest from small to large
        heapq.heappush(self.large, -heapq.heappop(self.small))
        # 3) Maintain size property: small may have one extra
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()