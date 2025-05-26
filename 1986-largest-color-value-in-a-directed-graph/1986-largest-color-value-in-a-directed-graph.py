class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = [[] for _ in range(n)]
        indeg = [0]*n
        
        # Build graph and indegree
        for u, v in edges:
            graph[u].append(v)
            indeg[v] += 1
        
        # dp[node] is an array[26] of max counts for each color up to that node
        dp = [[0]*26 for _ in range(n)]
        # Initialize dp for each node's own color
        for i, ch in enumerate(colors):
            dp[i][ord(ch) - ord('a')] = 1
        
        # Kahn's queue
        q = collections.deque([i for i in range(n) if indeg[i] == 0])
        seen = 0
        ans = 0
        
        while q:
            u = q.popleft()
            seen += 1
            # update global answer from dp[u]
            ans = max(ans, max(dp[u]))
            
            for v in graph[u]:
                # propagate dp[u] to dp[v]
                for c in range(26):
                    # if we take a path to v via u, count of color c at v
                    dp[v][c] = max(dp[v][c], dp[u][c] + (1 if c == (ord(colors[v]) - ord('a')) else 0))
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        
        # If we didn't process all nodes, there's a cycle
        if seen < n:
            return -1
        
        return ans