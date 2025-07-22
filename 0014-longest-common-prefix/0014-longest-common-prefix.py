class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Start with the first string as the maximum possible prefix
        prefix = strs[0]
        
        # Compare the prefix with each string
        for s in strs[1:]:
            # Shorten prefix until it matches the start of s
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # remove last char
                if not prefix:
                    return ""
        
        return prefix
        