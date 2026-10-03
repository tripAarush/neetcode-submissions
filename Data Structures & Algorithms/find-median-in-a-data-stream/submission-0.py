class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums = sorted(self.nums)
        if len(self.nums) % 2 == 1:
            return self.nums[len(self.nums)//2]
        else:
            return (self.nums[len(self.nums)//2] + self.nums[len(self.nums)//2-1]) / 2.0