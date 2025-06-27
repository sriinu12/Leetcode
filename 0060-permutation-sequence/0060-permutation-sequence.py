class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 1) Precompute factorials up to n
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i
        
        # 2) Initialize list of available digits
        digits = [str(i) for i in range(1, n + 1)]
        
        # 3) We build the (k-1)-indexed permutation
        k -= 1
        result = []
        
        for pos in range(n, 0, -1):
            # Determine which digit goes in the current position
            idx = k // fact[pos - 1]
            k %= fact[pos - 1]
            
            # Append and remove from the pool
            result.append(digits.pop(idx))
        
        # 4) Return as a concatenated string
        return ''.join(result)
        