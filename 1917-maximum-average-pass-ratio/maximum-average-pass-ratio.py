class Solution:
    def maxAverageRatio(
        self, classes: List[List[int]], extraStudents: int
    ) -> float:
        def _calculate_gain(passes, ts):
            return (passes + 1) / (ts + 1) - passes / ts

        max_heap = []
        for passes, ts in classes:
            gain = _calculate_gain(passes, ts)
            max_heap.append((-gain, passes, ts))

        heapq.heapify(max_heap)

        for _ in range(extraStudents):
            current_gain, passes, ts = heapq.heappop(max_heap)
            heapq.heappush(
                max_heap,
                (
                    -_calculate_gain(passes + 1, ts + 1),
                    passes + 1,
                    ts + 1,
                ),
            )

        tpr = sum(
            passes / ts for _, passes, ts in max_heap
        )
        return tpr / len(classes)