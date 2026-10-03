class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return None
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums)-1
        min_ele = float('inf')
        while right-left > 0:
            mid = (right - left) // 2 + left
            # the only time leftmost is smaller than right is sorted
            if nums[left] < nums[right]:
                return min(min_ele, nums[left])
            
            if nums[left] < nums[mid] or nums[mid] > nums[right]:
                left = mid + 1
                min_ele = min(nums[left], min_ele)
            else:
                right = mid
            min_ele = min(nums[mid], min_ele)
        
        return min_ele
            