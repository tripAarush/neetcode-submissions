class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        max_len = 0
        max_value = 0

        from collections import defaultdict
        hashmap = defaultdict(int)

        for r in range(len(s)):
            hashmap[s[r]] += 1
            max_value = max(max_value, max(hashmap.values()))
            while (r-l+1) - max_value > k:
                hashmap[s[l]]-=1
                l+=1
            max_len = max(r-l+1, max_len)
        
        return max_len