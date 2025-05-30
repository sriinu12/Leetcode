class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        
        def get_distances(start: int) -> List[int]:
            dist = [-1] * n
            d = 0
            cur = start
            # Follow the chain until end or revisit
            while cur != -1 and dist[cur] == -1:
                dist[cur] = d
                d += 1
                cur = edges[cur]
            return dist
        
        # Distances from node1 and node2
        dist1 = get_distances(node1)
        dist2 = get_distances(node2)
        
        # Find the node minimizing max(dist1[i], dist2[i])
        answer = -1
        best_cost = float('inf')
        
        for i in range(n):
            if dist1[i] != -1 and dist2[i] != -1:
                cost = max(dist1[i], dist2[i])
                # Choose smaller cost, then smaller index
                if cost < best_cost or (cost == best_cost and i < answer):
                    best_cost = cost
                    answer = i
        
        return answer
        