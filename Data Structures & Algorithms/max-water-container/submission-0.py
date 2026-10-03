class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_num = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                if (j-i) * min(heights[i], heights[j]) > max_num:
                    max_num = (j-i) * min(heights[i], heights[j])
        return max_num