class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res,cur_max, cur_min = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            cur_max,cur_min = max(nums[i], cur_max*nums[i], cur_min*nums[i]), min(nums[i], cur_max*nums[i], cur_min*nums[i])
            res = max(res, cur_max)
        
        return res