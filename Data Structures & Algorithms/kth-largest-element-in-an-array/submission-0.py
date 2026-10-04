class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from heapq import heapify, heappush, heappop
        heap = []

        for n in nums:
            heappush(heap, n)
            if len(heap) > k:
                heappop(heap)
        
        return heap[0]