class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_num = 0
        while left < right:
            max_num = max(max_num, min(heights[left], heights[right]) * (right-left))
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        return max_num
        # brute force
        # max_num = 0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         if (j-i) * min(heights[i], heights[j]) > max_num:
        #             max_num = (j-i) * min(heights[i], heights[j])
        # return max_num