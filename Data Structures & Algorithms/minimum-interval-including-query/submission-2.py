class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        from heapq import heappush, heappop
        intervals.sort()
        hashmap, i = {}, 0
        heap = []
        for q in sorted(queries):
            while i<len(intervals) and intervals[i][0]<=q:
                heappush(heap, (intervals[i][1]-intervals[i][0]+1, intervals[i][0], intervals[i][1]))
                i+=1
            
            while heap and heap[0][2] < q:
                heappop(heap)
            
            hashmap[q] = heap[0][0] if heap else -1

        res = []
        for q in queries:
            res.append(hashmap[q])
        return res

