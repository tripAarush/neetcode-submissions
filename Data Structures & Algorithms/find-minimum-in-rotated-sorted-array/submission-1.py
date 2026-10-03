class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0 or not nums:
            return None
        elif len(nums) == 1:
            return nums[0]

        min_num = float('inf')
        for i in range(1,len(nums), 2):
            min_num = min(min_num, min(nums[i], nums[i-1]))
            if i+1 == len(nums)-1:
                min_num = min(min_num, nums[i+1])
        
        return min_num