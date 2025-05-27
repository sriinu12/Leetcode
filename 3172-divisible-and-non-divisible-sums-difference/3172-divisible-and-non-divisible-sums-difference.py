class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
         # 1) Sum of all integers from 1 to n: n*(n+1)//2
        total_sum = n * (n + 1) // 2
        
        # 2) Count of multiples of m in [1..n] is k = n // m
        k = n // m
        
        # 3) Sum of multiples of m: m * (1 + 2 + ... + k)
        #    The sum 1+2+...+k = k*(k+1)//2
        divisible_sum = m * (k * (k + 1) // 2)
        
        # 4) Sum of non-divisible = total_sum - divisible_sum
        non_divisible_sum = total_sum - divisible_sum
        
        # 5) Return difference: non-divisible sum minus divisible sum
        return non_divisible_sum - divisible_sum
        