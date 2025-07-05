class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # 1) Count frequencies
        freq = Counter(arr)
        
        # 2) Check values in descending order for the “lucky” condition
        #    (only numbers ≤ len(arr) can possibly satisfy freq[x] == x)
        n = len(arr)
        ans = -1
        for x in range(min(n, max(freq.keys())) , 0, -1):
            if freq.get(x, 0) == x:
                return x
        
        # 3) None found
        return -1
        