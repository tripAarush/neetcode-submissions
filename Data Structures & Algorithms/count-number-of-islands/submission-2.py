class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        def dfs(visited, i, j):
            if i not in range(0,len(grid)) or j not in range(0,len(grid[0])) or (i,j) in visited or grid[i][j]=="0":
                return
            
            visited.add((i,j))
            dfs(visited, i+1, j)
            dfs(visited, i, j+1)
            dfs(visited, i-1, j)
            dfs(visited, i, j-1)
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j]=="1":
                    res+=1
                    dfs(visited,i,j)
        
        return res

            
            