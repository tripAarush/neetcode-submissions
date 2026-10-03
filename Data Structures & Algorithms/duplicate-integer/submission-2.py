class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            seen.add(n)
        if len(seen)!=len(nums):
            return True
        return False
        from collections import Counter
        res = Counter(nums)
        for n in res.values():
            if n>1:
                return True
        return False