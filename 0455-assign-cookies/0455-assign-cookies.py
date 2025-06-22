class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 1. Sort greed factors and cookie sizes
        g.sort()
        s.sort()

        # 2. Two pointers
        i = j = 0
        content = 0

        # 3. Greedily match
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                # assign cookie j to child i
                content += 1
                i += 1
                j += 1
            else:
                # cookie j too small, try next cookie
                j += 1

        return content
        