class Solution:
    def reverse(self, x: int) -> int:
        high = pow(2,31)-1
        low = pow(2,31)
        
        limit = low if x<0 else high
        x=abs(x)
        res = 0
        while x>0:
            rem = x%10
            if res>limit//10 or (res==limit//10 and rem>limit%10):
                return 0
            res=res*10+x%10
            x//=10
            
        
        return res if limit == high else -1*res
        
        

