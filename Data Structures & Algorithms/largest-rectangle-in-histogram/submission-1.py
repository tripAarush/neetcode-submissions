class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for idx, h in enumerate(heights):
            cur_idx = idx
            while stack and h<stack[-1][0]:
                prev_h, prev_idx = stack.pop()
                cur_idx = prev_idx
                res = max(res, prev_h * (idx-prev_idx))
            if not stack or h>stack[-1][0]:
                stack.append((h, cur_idx))
        while stack:
            h, idx = stack.pop()
            res = max(res, h * (len(heights)-idx))
        
        return res
            
        
        # # brute force for each value go left and right until there is something lower so you get bounds of width and calculate area for it
        
        # res = 0
        # for i, h in enumerate(heights):
        #     left_count = 0
        #     right_count = 0
        #     cur = i
        #     while cur-1 >= 0 and heights[cur-1] >= h:
        #         left_count+=1
        #         cur-=1
        #     cur = i
        #     while cur+1 < len(heights) and heights[cur+1] >= h:
        #         right_count+=1
        #         cur+=1
            
        #     res = max(res, h*(left_count+right_count+1))
        
        # return res