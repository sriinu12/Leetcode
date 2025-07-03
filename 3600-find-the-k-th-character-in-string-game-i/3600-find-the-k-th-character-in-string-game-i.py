class Solution:
    def kthCharacter(self, k: int) -> str:
        # popcnt = number of 1-bits in (k-1)
        # ord('a') + popcnt gives the ASCII code of the answer
        return chr(ord('a') + (k - 1).bit_count())
        