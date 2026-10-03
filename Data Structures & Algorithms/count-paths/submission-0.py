class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from collections import deque
        dp = [[0]*n for _ in range(m)]
        dp[0][0]=1

        deq = deque([(0,0)])
        visited = set()
        while deq:
            row,col = deq.popleft()

            if row-1 in range(m):
                dp[row][col] += dp[row-1][col]
            if col-1 in range(n):
                dp[row][col] += dp[row][col-1]
            
            if row+1 in range(m) and (row+1,col) not in visited:
                deq.append((row+1,col))
                visited.add((row+1,col))
            if col+1 in range(n) and (row,col+1) not in visited:
                deq.append((row,col+1))
                visited.add((row,col+1))

        return dp[m-1][n-1]