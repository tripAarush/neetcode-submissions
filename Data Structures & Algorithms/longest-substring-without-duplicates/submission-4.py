class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        left, right, tot = 0, 0, 0
        counter = defaultdict(int)
        if not s:
            return 0

        while right < len(s):
            counter[s[right]] += 1
            while counter[s[right]] > 1:
                if counter[s[left]] <= 1:
                    del counter[s[left]]
                else:
                    counter[s[left]]-=1
                left+=1
            tot = max(tot, len(counter))
            right+=1
        
        return tot