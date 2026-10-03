class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values = set()
        for i in range(len(nums)):
            values.add(nums[i])
        
        if len(values) == len(nums):
            return False
        return True
