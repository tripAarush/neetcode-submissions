class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        freq = [0] * 26
        for s in s1:
            freq[ord(s)-ord('a')] += 1
        cur = [0] * 26
        left, right =0,len(s1)-1
        for i in range(len(s1)):
            cur[ord(s2[i])-ord('a')] += 1
        
        while right<len(s2):
            if cur == freq:
                return True
            cur[ord(s2[left])-ord('a')]-=1
            left+=1
            right+=1
            if right<len(s2):
                cur[ord(s2[right])-ord('a')]+=1
        
        return False

            