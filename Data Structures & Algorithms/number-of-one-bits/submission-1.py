class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            # see if rightmost 1 or 0
            res+=n&1
            n>>=1 #get rid of rightmost bit
        
        return res

