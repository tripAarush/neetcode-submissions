class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*len(s)
        dp.append(1)

        for i in range(len(dp)-2,-1,-1):
            if s[i] == '0':
                dp[i] == 0
                continue
            if i+1<len(s) and (s[i] == '1' or s[i]=='2' and s[i+1] in '0123456'):
                dp[i] = dp[i+1] + dp[i+2]
            else:
                dp[i] = dp[i+1]
        
        return dp[0]





        # dp = {len(s):1}

        # def dfs(i):
        #     if i in dp:
        #         return dp[i]
        #     if s[i] == '0':
        #         return 0
        #     res = dfs(i+1)
        #     if i+1<len(s) and (s[i]=='1' or s[i]=='2' and s[i+1] in '0123456'):
        #         dp[i]=dfs(i+1)+dfs(i+2)
        #     else:
        #         dp[i] = dfs(i+1)
        #     return dp[i]
        
        # return dfs(0)
