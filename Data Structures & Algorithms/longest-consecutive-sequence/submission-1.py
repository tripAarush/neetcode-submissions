class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        check = set(nums)
        tot = 0

        for n in nums:
            if n-1 in check:
                continue
            else:
                start = n
                count = 1
                while start+1 in check:
                    count+=1
                    start+=1
                tot = max(tot,count)
        
        return tot