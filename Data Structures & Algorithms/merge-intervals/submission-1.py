class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        
        res = []
        idx = 1

        while (idx<len(intervals)):
            if (intervals[idx][0] <= intervals[idx-1][1]):
                intervals[idx] = [intervals[idx-1][0], max(intervals[idx][1], intervals[idx-1][1])]
            else:
                res.append(intervals[idx-1])
            idx+=1
        res.append(intervals[-1])
        return res