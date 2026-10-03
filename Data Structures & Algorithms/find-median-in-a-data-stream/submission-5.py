from heapq import heappush, heappop, heapify
class MedianFinder:
    def __init__(self):
        self.upper = []
        self.lower = []

    def balance(self,upper,lower):
        while len(self.lower) - len(self.upper) > 1:
            low = -1*heappop(self.lower)
            heappush(self.upper, low)
        while len(self.upper) - len(self.lower) > 1:
            up = -1*heappop(self.upper)
            heappush(self.lower, up)

    def addNum(self, num: int) -> None:
        if not self.lower or not self.upper:
            if self.lower:
                if num > -1*self.lower[0]:
                    heappush(self.upper,num)
                else:
                    low = -1*heappop(self.lower)
                    heappush(self.upper, low)
                    heappush(self.lower, -1*num)
            elif self.upper:
                if num < self.upper[0]:
                    heappush(self.lower,-1*num)
                else:
                    up = heappop(self.upper)
                    heappush(self.lower, -1*up)
                    heappush(self.upper, num)
            else:
                heappush(self.lower, -1*num)
            return

        if -1*self.lower[0] > num:
            heappush(self.lower,-1*num)
        else:
            heappush(self.upper,num)
        self.balance(self.upper, self.lower)

    def findMedian(self) -> float:
        if len(self.lower)==len(self.upper):
            return (-1*self.lower[0] + self.upper[0]) / 2
        elif len(self.lower)>len(self.upper):
            return -1*self.lower[0]
        else:
            return self.upper[0]








        