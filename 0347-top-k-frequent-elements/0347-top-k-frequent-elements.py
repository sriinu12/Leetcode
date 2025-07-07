class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequencies
        freq = Counter(nums)
        n = len(nums)
        
        # 2. Create buckets: index i holds a list of nums that appear i times
        buckets = [[] for _ in range(n + 1)]
        for num, cnt in freq.items():
            buckets[cnt].append(num)
        
        # 3. Collect from high to low frequency
        res: List[int] = []
        for count in range(n, 0, -1):
            for num in buckets[count]:
                res.append(num)
                if len(res) == k:
                    return res
        return res  # (k is guaranteed ≤ #unique, so we’ll always return inside the loop)
        