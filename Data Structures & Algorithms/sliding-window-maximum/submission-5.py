class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from heapq import heapify, heappush, heappop
        if k > len(nums):
            return []
        nums = [-1*num for num in nums]
        heap = []
        for idx, num in enumerate(nums[0:k]):
            heap.append((num,idx))
        heapify(heap)
        res = [-1*heap[0][0]]

        for idx in range(k, len(nums)):
            while heap and heap[0][1] <= idx-k:
                heappop(heap)
            heappush(heap, (nums[idx], idx))
            res.append(-1*heap[0][0])
        
        return res


        # wind = []
        # left, right = 0, k-1
        # if k > len(nums):
        #     return []
        # res = []

        # while right<len(nums):
        #     res.append(max(nums[left:right+1]))
        #     right+=1
        #     left+=1

        # return res