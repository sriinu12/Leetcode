class Solution:
    def romanToInt(self, s: str) -> int:
       # 1. Value mapping
        values = {
            'I': 1, 'V': 5,
            'X': 10, 'L': 50,
            'C': 100, 'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        # 2. Iterate characters
        for i in range(n):
            # Look ahead if this symbol is a subtractive pair
            if i + 1 < n and values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        
        return total 
        