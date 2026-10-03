class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        p2 = 0
        distinct = set()

        max_len = 0
        while p2<len(s):
            if s[p2] in distinct:
                distinct.remove(s[p1])
                p1+=1
                continue
            
            distinct.add(s[p2])
            p2+=1
            max_len = max(max_len, len(distinct))

        return max_len
            