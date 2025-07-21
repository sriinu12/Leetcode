class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        i, n = 0, len(s)
        # 1) Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # 2) Handle optional sign
        sign = 1
        if i < n and s[i] in ('+', '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        # 3) Convert digits to number
        result = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            
            # 4) Check overflow
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            i += 1
        
        return sign * result
        