class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        from heapq import heapify, heappush, heappop
        heap = []
        heapify(heap)
        cur_p = 0
        trips.sort(key=lambda x:x[1])
        for num_p, fro, to in trips:
            cur_p += num_p
            while heap and fro >= heap[0][0]:
                _, old_p = heappop(heap)
                cur_p-=old_p

            heappush(heap, (to, num_p))

            if cur_p > capacity:
                return False

        return True