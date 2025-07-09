class Solution:
    def isValid(self, s: str) -> bool:
        # Mapping from closing to opening brackets
        match = {')': '(', ']': '[', '}': '{'}
        stack = []
        
        for c in s:
            if c in match:
                # c is a closing bracket: check top of stack
                if not stack or stack[-1] != match[c]:
                    return False
                stack.pop()
            else:
                # c is an opening bracket
                stack.append(c)
        
        # Valid if no unclosed openings remain
        return not stack
        