class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use a heap of size k and hashmap to track frequency
        from heapq import heappush, heappop
        from collections import defaultdict

        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num]+=1
        
        heap = []
        
        for val, count in hashmap.items():
            heappush(heap, (count, val))
            while len(heap) > k:
                heappop(heap)
        
        return [key for _, key in heap]
        