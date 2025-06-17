class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # Precompute factorials and inverses up to n-1
        fact = [1] * (n)
        for i in range(1, n):
            fact[i] = fact[i-1] * i % MOD
        
        invfact = [1] * (n)
        invfact[n-1] = pow(fact[n-1], MOD-2, MOD)
        for i in range(n-1, 0, -1):
            invfact[i-1] = invfact[i] * i % MOD
        
        # Compute C(n-1, k)
        if k < 0 or k > n-1:
            return 0
        comb = fact[n-1] * invfact[k] % MOD * invfact[n-1-k] % MOD
        
        # Compute (m-1)^(n-1-k)
        pow_term = pow(m-1, n-1-k, MOD)
        
        # Final result
        return m * comb % MOD * pow_term % MOD
        