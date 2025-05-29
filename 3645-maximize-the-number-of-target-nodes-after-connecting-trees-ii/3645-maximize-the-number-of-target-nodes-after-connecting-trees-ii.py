class Solution:
    def bfs(self,
            start: int,
            adj: List[List[int]],
            included: Optional[List[bool]] = None
           ) -> int:
        """
        Single BFS that:
          1) Returns the count of nodes at even-numbered levels.
          2) If `included` is provided, marks included[i]=True for each node i at an even level.
        """
        q = deque([(start, -1)])
        level = 0
        count = 0
        while q:
            size = len(q)
            # At even levels, add to count and optionally record nodes
            if level % 2 == 0:
                count += size
            for _ in range(size):
                node, parent = q.popleft()
                if included is not None and level % 2 == 0:
                    included[node] = True
                for nei in adj[node]:
                    if nei != parent:
                        q.append((nei, node))
            level += 1
        return count
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n1 = len(edges1) + 1
        n2 = len(edges2) + 1
        adj1 = [[] for _ in range(n1)]
        adj2 = [[] for _ in range(n2)]
        for u, v in edges1:
            adj1[u].append(v); adj1[v].append(u)
        for u, v in edges2:
            adj2[u].append(v); adj2[v].append(u)

        # Step 1: Best possible from Tree 2
        even2 = self.bfs(0, adj2)
        odd2 = n2 - even2
        best2 = max(even2, odd2)

        # Step 2: Record which nodes in Tree 1 are at even levels
        included = [False] * n1
        even1 = self.bfs(0, adj1, included)
        odd1 = n1 - even1

        # Step 3: Combine for each node in Tree 1
        ans = [0] * n1
        for i in range(n1):
            ans[i] = (even1 if included[i] else odd1) + best2

        return ans
        