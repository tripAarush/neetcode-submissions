class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        queue = deque()
        rows, cols = len(grid), len(grid[0])

        inf = 2147483647

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j))

        while queue:
            r, c = queue.popleft()
            
            for nr, nc in ((1,0),(-1,0),(0,-1),(0,1)):
                if r+nr in range(rows) and c+nc in range(cols) and grid[r+nr][c+nc] == inf:
                    grid[r+nr][c+nc] = grid[r][c] + 1
                    queue.append((r+nr, c+nc))
        
        #queue = [(0,2), (3,0)]
        #[(3,0),(1,2),(0,3), (2,0)]
        return


                    

