from heapq import heapify, heappush, heappop
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.top_k = []
        self.k = k
        for i in range(len(nums)):
            heappush(self.top_k, nums[i])
            if len(self.top_k) > k:
                heappop(self.top_k)

    def add(self, val: int) -> int:
        if len(self.top_k) < self.k:
            heappush(self.top_k, val)
        elif val > self.top_k[0]:
            heappop(self.top_k)
            heappush(self.top_k, val)
        
        return self.top_k[0]
