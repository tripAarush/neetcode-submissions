from heapq import heappush, heappop, heapify
class MedianFinder:
    def __init__(self):
        self.upper = []
        self.lower = []

    def balance(self):
        while len(self.lower) - len(self.upper) > 1:
            low = -1*heappop(self.lower)
            heappush(self.upper, low)
        while len(self.upper) - len(self.lower) > 1:
            up = -1*heappop(self.upper)
            heappush(self.lower, up)

    def addNum(self, num: int) -> None:
        if not self.lower or -1*self.lower[0]>num:
            heappush(self.lower,-1*num)
        else:
            heappush(self.upper,num)
        self.balance()

    def findMedian(self) -> float:
        if len(self.lower)==len(self.upper):
            return (-1*self.lower[0] + self.upper[0]) / 2
        elif len(self.lower)>len(self.upper):
            return -1*self.lower[0]
        else:
            return self.upper[0]








        