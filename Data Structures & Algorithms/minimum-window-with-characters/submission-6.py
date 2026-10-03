class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        from collections import defaultdict
        count, cur = defaultdict(int), defaultdict(int)
        for ch in t:
            count[ch]+=1
        left = 0
        have, need = 0, len(count)
        res_len = float('inf')
        res = ""
        for right in range(len(s)):
            if s[right] in count:
                cur[s[right]]+=1
                if count[s[right]] == cur[s[right]]:
                    have+=1
            
            while have == need:
                if right-left+1 < res_len:
                    res_len = right-left+1
                    res = s[left:right+1]

                if s[left] in count:
                    cur[s[left]]-=1
                    if cur[s[left]] < count[s[left]]:
                        have-=1
                left+=1
        return res
            
