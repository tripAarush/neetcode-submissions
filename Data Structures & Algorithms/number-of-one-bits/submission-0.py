class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 1:
            return 1
        c = 0
        while n>=pow(2,c):
            c+=1

        c-=1
        res = 0
        while c>=0:
            if n>=pow(2,c):
                res +=1
                n-=pow(2,c)
            c-=1
        return res

