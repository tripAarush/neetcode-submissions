class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic = set()
        pacific = set()
        def dfs(r,c,ocean,last):
            if (r,c) in ocean:
                return
            if r in range(len(heights)) and c in range(len(heights[0])): 
                if heights[r][c] >= last:
                    ocean.add((r,c))
                    dfs(r+1,c,ocean,heights[r][c])
                    dfs(r-1,c,ocean,heights[r][c])
                    dfs(r,c+1,ocean,heights[r][c])
                    dfs(r,c-1,ocean,heights[r][c])
    
            
        for r in range(len(heights)):
            dfs(r,0,pacific,0)
            dfs(r,len(heights[0])-1,atlantic,0)
        
        for c in range(len(heights[0])):
            dfs(0,c,pacific,0)
            dfs(len(heights)-1,c,atlantic,0)
        
        return list(atlantic & pacific)
