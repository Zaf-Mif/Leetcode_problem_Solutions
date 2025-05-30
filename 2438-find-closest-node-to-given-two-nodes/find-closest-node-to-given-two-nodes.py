from typing import List

class Solution:
    def explore_path(self, current: int, graph: List[int], distances: List[int], visited: List[bool]):
        visited[current] = True
        next_node = graph[current]
        if next_node != -1 and not visited[next_node]:
            distances[next_node] = distances[current] + 1
            self.explore_path(next_node, graph, distances, visited)

    def closestMeetingNode(self, graph: List[int], startA: int, startB: int) -> int:
        n = len(graph)

        distance_from_A = [float('inf')] * n
        distance_from_B = [float('inf')] * n
        visited_from_A = [False] * n
        visited_from_B = [False] * n

        distance_from_A[startA] = 0
        distance_from_B[startB] = 0

        self.explore_path(startA, graph, distance_from_A, visited_from_A)
        self.explore_path(startB, graph, distance_from_B, visited_from_B)

        best_node = -1
        minimal_max_distance = float('inf')

        for node in range(n):
            max_distance = max(distance_from_A[node], distance_from_B[node])
            if max_distance < minimal_max_distance:
                minimal_max_distance = max_distance
                best_node = node

        return best_node
