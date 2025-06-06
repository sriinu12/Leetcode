class Solution:
    def robotWithString(self, s: str) -> str:
        # Count frequency of each character in s
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # Helper to get the smallest character still remaining in s
        def get_min_remaining() -> str:
            for i in range(26):
                if freq[i] > 0:
                    return chr(i + ord('a'))
            return '{'  # character after 'z' in ASCII, so any real char <= this

        t_stack = []     # simulate the robot's held string t
        result = []      # characters written to paper
        min_char = get_min_remaining()

        for ch in s:
            # Move ch from s → t
            t_stack.append(ch)
            freq[ord(ch) - ord('a')] -= 1

            # Update min_char to the smallest still in s
            min_char = get_min_remaining()

            # While t_stack’s top can be written (i.e. top <= min_char), pop it out
            while t_stack and t_stack[-1] <= min_char:
                result.append(t_stack.pop())

        # Once s is exhausted, flush any remaining characters from t_stack
        while t_stack:
            result.append(t_stack.pop())

        return "".join(result)
        