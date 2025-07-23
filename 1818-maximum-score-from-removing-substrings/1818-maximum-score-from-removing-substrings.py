class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # Determine which pattern to remove first
        # If x >= y, remove "ab" first; else remove "ba" first
        first_pat, first_val = ("ab", x) if x >= y else ("ba", y)
        second_pat, second_val = ("ba", y) if x >= y else ("ab", x)
        
        score = 0
        
        # Pass 1: remove all occurrences of first_pat
        stack1 = []
        a, b = first_pat  # e.g. ('a', 'b') for "ab"
        for c in s:
            if stack1 and stack1[-1] == a and c == b:
                # We have found the pattern
                stack1.pop()
                score += first_val
            else:
                stack1.append(c)
        
        # Build intermediate string after high‑value removals
        t = "".join(stack1)
        
        # Pass 2: remove all occurrences of second_pat
        stack2 = []
        a2, b2 = second_pat
        for c in t:
            if stack2 and stack2[-1] == a2 and c == b2:
                stack2.pop()
                score += second_val
            else:
                stack2.append(c)
        
        return score
        