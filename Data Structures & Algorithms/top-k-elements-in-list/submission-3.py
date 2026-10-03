class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #instead of heap we can use freq list
        from collections import defaultdict
        count = defaultdict(int)
        for n in nums:
            count[n]+=1
        freq = [[] for _ in range(len(nums))]

        for n, c in count.items():
            freq[c-1].append(n)
        
        freq.reverse()
        res = []
        for nums in freq:
            for num in nums:
                res.append(num)
                if len(res)==k:
                    return res


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
        