class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        # Number of doubling/appending steps we need to consider
        opsCount = math.ceil(math.log2(k))
        increases = 0

        # Reverse-simulate which half k comes from at each step
        for i in range(opsCount - 1, -1, -1):
            half = 1 << i
            if k > half:
                k -= half
                increases += operations[i]

        # 'a' shifted increases times (mod 26)
        return chr(ord('a') + (increases % 26))
        