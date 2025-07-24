class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        # 1) Compute total XOR
        total = functools.reduce(operator.xor, nums, 0)

        # 2) Build adjacency list
        tree = [[] for _ in range(n)]
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        # 3) Initialize subtree XORs and descendant sets
        subXor = nums[:]               # subXor[u] = XOR of u's subtree
        descendants = [{i} for i in range(n)]

        # 4) DFS to fill subXor[] and descendants[]
        def dfs(u: int, parent: int) -> tuple[int, set[int]]:
            for v in tree[u]:
                if v == parent:
                    continue
                vx, vdesc = dfs(v, u)
                subXor[u] ^= vx
                descendants[u] |= vdesc
            return subXor[u], descendants[u]

        dfs(0, -1)

        # 5) Try every pair of edges to remove
        ans = math.inf
        m = len(edges)
        for i in range(m):
            a, b = edges[i]
            # ensure 'a' is the parent side: b in descendants[a]
            if b in descendants[a]:
                a, b = b, a
            for j in range(i):
                c, d = edges[j]
                if d in descendants[c]:
                    c, d = d, c

                # Determine the three component XORs based on containment
                if c in descendants[a] and a != c:
                    c1 = subXor[c]
                    c2 = subXor[a] ^ subXor[c]
                    c3 = total       ^ subXor[a]
                elif a in descendants[c] and a != c:
                    c1 = subXor[a]
                    c2 = subXor[c] ^ subXor[a]
                    c3 = total       ^ subXor[c]
                else:
                    c1 = subXor[a]
                    c2 = subXor[c]
                    c3 = total ^ subXor[a] ^ subXor[c]

                score = max(c1, c2, c3) - min(c1, c2, c3)
                ans = min(ans, score)

        return ans
        