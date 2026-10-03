class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i=0
        while i <len(nums):
            while i!=0 and i<len(nums) and nums[i]==nums[i-1]:
                i+=1
            left = i+1
            right = len(nums)-1
            while right>left:
                if nums[left] + nums[right] < -nums[i]:
                    left+=1
                elif nums[left] + nums[right] > -nums[i]:
                    right-=1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    while left<len(nums) and nums[left]==nums[left-1]:
                        left+=1
                    right-=1
            i+=1

        return res