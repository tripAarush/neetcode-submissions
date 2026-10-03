class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from heapq import heapify, heappush, heappop
        heap = []

        for p in points:
            dist = pow((pow(p[0], 2) + pow(p[1], 2)), 0.5)
            if len(heap) < k:
                heappush(heap, (-1*dist, p))
            elif heap[0][0] * -1 > dist:
                heappush(heap, (-1*dist, p))
                heappop(heap)
        
        return [x[1] for x in heap]