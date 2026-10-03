class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        starts = set()
        check = set(nums)
        tot = 0

        for n in nums:
            if n-1 in check:
                continue
            else:
                starts.add(n)
        
        for start in starts:
            i = start
            count = 1
            while i+1 in check:
                count+=1
                i+=1
            tot = max(tot, count)
        
        return tot