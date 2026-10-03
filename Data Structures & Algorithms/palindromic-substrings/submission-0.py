class Solution:
    def countSubstrings(self, s: str) -> int:
        tot = 0
        for i in range(len(s)):
            # odd length
            l,r=i,i
            while l>=0 and r<len(s) and s[r]==s[l]:
                tot+=1
                l-=1
                r+=1
            
            #even length
            l,r=i,i+1
            while l>=0 and r<len(s) and s[r]==s[l]:
                tot+=1
                l-=1
                r+=1
        
        return tot