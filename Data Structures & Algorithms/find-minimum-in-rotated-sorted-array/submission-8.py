class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if right and left > mid, min from left to mid
        # if left < mid < right, min = left
        # if right < mid and left > mid, mind from mid to right
        left, right = 0, len(nums)-1
        while right > left:
            mid = (right+left)//2
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right=mid

        return nums[right]

        while right > left:
            mid = (right+left) // 2
            if nums[left] <= nums[mid] <= nums[right]:
                return nums[left]
            elif nums[left] >= nums[mid] and nums[right] >= nums[mid]:
                right = mid
            else:
                left = mid+1
        
        return nums[right]
        