class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ' c r a '
        ' c b a'
        # [[1 0 0], [0 0 0], [0 0 2]]

        dp = [[0]* len(text2) for _ in range(len(text1))]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i]==text2[j]:
                    if i-1<0 or j-1<0:
                        dp[i][j] = 1
                    else: dp[i][j] = dp[i-1][j-1]+1
                else:
                    if i-1<0 and j-1<0:
                        dp[i][j] = 0
                    elif i-1<0:
                        dp[i][j] = dp[i][j-1]
                    elif j-1<0:
                        dp[i][j] = dp[i-1][j]
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]
                

        # res = 0
        # cur = 0
        # def dfs(idx1, idx2, cur):
        #     if idx1 >= len(text1) or idx2>=len(text2):
        #         return
        #     nonlocal res
        #     if text1[idx1] == text2[idx2]:
        #         cur+=1
        #         res = max(res,cur)
        #         dfs(idx2+1, idx2+1, cur)
        #     else:
        #         dfs(idx1, idx2+1,cur)
        #         dfs(idx1+1, idx2,cur)

        # dfs(0,0,0)
        # return res