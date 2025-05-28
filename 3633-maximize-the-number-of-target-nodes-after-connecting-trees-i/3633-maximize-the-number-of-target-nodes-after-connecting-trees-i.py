from collections import deque
from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        # build adjacency lists
        n = len(edges1) + 1
        m = len(edges2) + 1

        adj1 = [[] for _ in range(n)]
        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)

        adj2 = [[] for _ in range(m)]
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        # helper: BFS from each node to compute counts of nodes within distance D
        def compute_within_distance(adj: List[List[int]], max_dist: int) -> List[int]:
            size = len(adj)
            counts = [0] * size
            for src in range(size):
                dist = [-1] * size
                q = deque([src])
                dist[src] = 0
                cnt = 0
                while q:
                    u = q.popleft()
                    if dist[u] > max_dist:
                        continue
                    cnt += 1
                    for w in adj[u]:
                        if dist[w] < 0:
                            dist[w] = dist[u] + 1
                            q.append(w)
                counts[src] = cnt
            return counts

        # count1[i] = # nodes in tree1 within distance <= k from i
        count1 = compute_within_distance(adj1, k)
        # count2[j] = # nodes in tree2 within distance <= k-1 from j
        if k > 0:
            count2 = compute_within_distance(adj2, k - 1)
            max2 = max(count2)
        else:
            # cannot reach any node in tree2 if k == 0
            max2 = 0

        # for each i in tree1, best we can do is count1[i] + max2
        return [c1 + max2 for c1 in count1]
