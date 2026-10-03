class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        from heapq import heapify, heappush, heappop
        heap = []
        for s in stones:
            heappush(heap, s*-1)

        while len(heap) > 1:
            x = heappop(heap)
            y = heappop(heap)
            if y > x:
                heappush(heap, x-y)

        return heap[0]*-1 if heap else 0       