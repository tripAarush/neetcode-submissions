class MedianFinder:

    def __init__(self):
        self.nums = []
        self.large, self.small = [], []

    def addNum(self, num: int) -> None:
        # making it a max heap
        # adding/removing value from heap is o(logn), 
        heapq.heappush(self.small, -1 * num)

        # have to make sure that every element in small <= large
        if self.small and self.large and (self.small[0] * -1) > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        self.nums.append(num)

        #cant have the size of the heaps more than one different
        if len(self.large) > len(self.small) +1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (self.small[0] * -1 + self.large[0]) / 2.0
        