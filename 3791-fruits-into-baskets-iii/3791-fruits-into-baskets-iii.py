class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        # Build size = next power of two ≥ n
        size = 1
        while size < n:
            size <<= 1
        # segment tree array, 1-indexed
        tree = [0] * (2 * size)
        
        # 1) Initialize leaves
        for i in range(n):
            tree[size + i] = baskets[i]
        # 2) Build internal nodes
        for i in range(size - 1, 0, -1):
            tree[i] = max(tree[2*i], tree[2*i + 1])
        
        def find_and_remove(target: int) -> bool:
            """Return True if placed (and remove it), else False."""
            if tree[1] < target:
                return False
            idx = 1
            # Descend to leaf
            while idx < size:
                # Prefer left child if it can fit
                if tree[2*idx] >= target:
                    idx = 2*idx
                else:
                    idx = 2*idx + 1
            # idx is now a leaf: remove it
            tree[idx] = -1
            # Bubble update up
            idx //= 2
            while idx:
                tree[idx] = max(tree[2*idx], tree[2*idx + 1])
                idx //= 2
            return True
        
        unplaced = 0
        for f in fruits:
            if not find_and_remove(f):
                unplaced += 1
        
        return unplaced
        