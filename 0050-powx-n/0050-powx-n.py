class Solution:
    def myPow(self, x: float, n: int) -> float:
        N = n
        if N < 0:
            x = 1/x
            N = -N
        result = 1
        current_prod = x
        while N>0:
            if N & 1:
                result *= current_prod
            current_prod *= current_prod
            N >>= 1
        return result

        