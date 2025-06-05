class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # DSU (Disjoint Set Union) for 26 lowercase letters
        parent = list(range(26))
        
        def find(x: int) -> int:
            # Path‐compression find
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x: int, y: int) -> None:
            # Union by always attaching the larger‐letter root to the smaller‐letter root
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rx < ry:
                parent[ry] = rx
            else:
                parent[rx] = ry
        
        # Step 1: Build equivalences from s1 and s2
        for a, b in zip(s1, s2):
            union(ord(a) - ord('a'), ord(b) - ord('a'))
        
        # Step 2: For each character in baseStr, replace with the lexicographically smallest in its set
        result_chars = []
        for ch in baseStr:
            root = find(ord(ch) - ord('a'))
            smallest_equiv_char = chr(root + ord('a'))
            result_chars.append(smallest_equiv_char)
        
        return "".join(result_chars)
        