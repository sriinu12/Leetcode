class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        oddN, evenN = (n + 1) // 2, n // 2
        oddM, evenM = (m + 1) // 2, m // 2
        return oddN * evenM + evenN * oddM
        