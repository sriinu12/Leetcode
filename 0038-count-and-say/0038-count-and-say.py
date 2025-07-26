class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        res = "1"
        # Build sequence from 2 to n
        for _ in range(2, n + 1):
            prev = res
            builder = []
            i = 0
            length = len(prev)
            
            # Process groups in prev
            while i < length:
                j = i + 1
                # Count how many times prev[i] repeats
                while j < length and prev[j] == prev[i]:
                    j += 1
                count = j - i
                # Append "<count><digit>"
                builder.append(str(count))
                builder.append(prev[i])
                # Move to the next new digit
                i = j
            
            # Join parts to form next term
            res = "".join(builder)
        
        return res
        