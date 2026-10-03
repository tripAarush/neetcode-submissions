class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        hashmap = defaultdict(int)
        left, right = 0, 0
        res = 0

        while right<len(s):
            hashmap[s[right]] += 1
            while right-left+1 - max(hashmap.values()) > k:
                hashmap[s[left]]-=1
                left+=1
            
            res = max(res, right-left+1)
            right+=1
        return res