class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n < 2:
            return 1
        
        cnt = 0
        graph = defaultdict(set)

        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)
        
        queue = deque(
            node for node, neighbors in graph.items() if len(neighbors) == 1
        )

        while queue:
            curr = queue.popleft()
            nbr = (
                next(iter(graph[curr])) if graph[curr] else -1
            )

            if nbr >= 0:
                graph[nbr].remove(curr)

            if values[curr] % k == 0:
                cnt += 1
            else:
                values[nbr] += values[curr]
        

            if nbr >= 0 and len(graph[nbr]) == 1:
                queue.append(nbr)

        return cnt
