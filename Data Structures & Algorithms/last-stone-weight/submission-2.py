class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        from heapq import heapify, heappush, heappop
        heap = [-1*s for s in stones]
        heapify(heap)

        while len(heap) > 1:
            x = heappop(heap)
            y = heappop(heap)
            if y > x:
                heappush(heap, x-y)

        return heap[0]*-1 if heap else 0       