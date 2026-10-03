class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0 or not nums:
            return None
        elif len(nums) == 1:
            return nums[0]

        while len(nums) > 1:
            new_nums = []

            for i in range(0, len(nums), 2):
                if i+1 == len(nums):
                    new_nums.append(nums[i])
                    continue                    
                new_nums.append(min(nums[i], nums[i+1]))
            nums = new_nums
        
        return nums[0]