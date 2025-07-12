class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        # DP state: (l, r, k) -> [earliest, latest]
        @functools.lru_cache(None)
        def dp(l: int, r: int, k: int) -> List[int]:
            # If they meet immediately
            if l == r:
                return [1, 1]
            # Ensure l < r
            if l > r:
                return dp(r, l, k)
            
            earliest = math.inf
            latest   = -math.inf
            # Next round bracket size
            next_k = (k + 1) // 2
            
            # Enumerate possible match positions i, j in round 1
            for i in range(1, l + 1):
                # j must map r to one of the winners
                # r_index = (i + j) in [l+r - k//2 .. (k+1)//2]
                for j in range(l - i + 1, r - i + 1):
                    if not (l + r - k // 2 <= i + j <= next_k):
                        continue
                    sub_earliest, sub_latest = dp(i, j, next_k)
                    earliest = min(earliest, sub_earliest + 1)
                    latest   = max(latest,   sub_latest   + 1)
            
            return [earliest, latest]

        # Map secondPlayer into "r from the end"
        return dp(firstPlayer, n - secondPlayer + 1, n)
        